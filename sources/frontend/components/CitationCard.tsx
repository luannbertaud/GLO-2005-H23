"use client";

import React, { useState, useEffect } from "react";
import Comment from "@/components/Comment";
import NewComment from "@/components/NewComment";
import { secondsToRelative } from "@/components/TimeParsing";
import { useCookies } from "react-cookie";
import { useRouter } from "next/navigation";
import { DynaPuff, Dancing_Script, Cinzel, Orbitron } from "next/font/google";

const dyna = DynaPuff({ subsets: ["latin"] });
const dancing = Dancing_Script({ subsets: ["latin"] });
const cinzel = Cinzel({ subsets: ["latin"] });
const orbit = Orbitron({ subsets: ["latin"] });

const FONT_FAMILIES = [
  [undefined, "Arial"],
  [`${dyna.className}`, "DynaPuff"],
  [`${dancing.className}`, "Dancing"],
  [`${cinzel.className}`, "Cinzel"],
  [`${orbit.className}`, "Orbitron"],
];

export default function CitationCard({ body, deleteCallback }: any) {
  const [userLiked, setUserLiked] = React.useState(body.user_like);
  const [commentsOpened, setCommentsOpened] = React.useState(false);
  const [card, setCard]: [any, any] = useState(body);
  const [cookies]: [any, any, any] = useCookies(["user"]);
  const commentsContainerRef = React.createRef<HTMLDivElement>();
  const router = useRouter();
  let cardFont = undefined;
  const [userIsAuthor, setUserIsAuthor]: [boolean, any] = useState(false);

  useEffect(() => {
    if (
      JSON.parse(
        Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
      ).username === body.author
    )
      setUserIsAuthor(true);
  }, [cookies, body.author, body.id]);

  for (let font of FONT_FAMILIES) {
    if (font[1] === body.police) cardFont = font[0];
  }

  /**
   * Posts the comment submitted at the dedicated post.
   *
   * @param content - Contains the comment's content
   */

  async function userComment(content: string) {
    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/comments`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
      body: JSON.stringify({
        body: content,
        post_id: card.id,
      }),
    });

    if (res.ok) {
      await res.json().then((j) => {
        setCard({
          ...card,
          comments: [j, ...card.comments],
        });
      });
    } else {
      await res.json().then((j) => {
        alert(j.desc);
      });
    }
  }

  /**
   * Removes the comment submitted by the user.
   *
   * @param comment_id - id of the published comment
   */

  async function userCommentDelete(comment_id: number) {
    let res = await fetch(
      `${process.env.NEXT_PUBLIC_API_HOST}/comments/${comment_id}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-token-id": JSON.parse(
            Buffer.from(cookies["ipaper_user_token"], "base64").toString(
              "ascii"
            )
          ).token_id,
        },
      }
    );

    if (res.ok) {
      await res.text().then((_) => {
        setCard({
          ...card,
          comments: [...card.comments.filter((c: any) => c.id !== comment_id)],
        });
      });
    } else {
      await res.text().then((r) => {
        alert(r);
      });
    }
  }

  /**
   * Adds a like to the chosen post.
   */

  async function userLike() {
    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/like`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
      body: JSON.stringify({ post_id: card.id }),
    });

    if (res.ok) {
      await res.text().then((_) => {
        setCard({ ...card, likes: card.likes + 1 });
        setUserLiked(true);
      });
    } else await res.text().then((r) => alert(r));
  }

  /**
   * Removes a like to the chosen post.
   */

  async function userUnLike() {
    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/like`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
      body: JSON.stringify({ post_id: card.id }),
    });

    if (res.ok) {
      await res.text().then((_) => {
        setCard({ ...card, likes: card.likes - 1 });
        setUserLiked(false);
      });
    } else await res.text().then((r) => alert(r));
  }

  async function handleLikeClick() {
    if (userLiked) await userUnLike();
    else await userLike();
  }

  /**
   * Allows you to display the comments left by users.
   */

  async function toggleComments() {
    const commentsContainer = commentsContainerRef.current;
    if (!commentsOpened) {
      commentsContainer!.style.maxHeight = "200px";
      commentsContainer!.style.padding = "1.25rem 0 1.25rem 0";
      setTimeout(() => {
        commentsContainer!.style.opacity = "1";
      }, 400);
    } else {
      commentsContainer!.style.opacity = "0";
      setTimeout(() => {
        commentsContainer!.style.maxHeight = "0";
        commentsContainer!.style.padding = "0";
      }, 400);
    }
    setCommentsOpened(!commentsOpened);
  }

  return (
    <div className="flex h-fit w-full max-w-2xl flex-col gap-5 rounded-2xl p-5 pt-7 font-mono shadow-2xl max-h-md">
      <div className="flex justify-between">
        <button
          className={
            "w-fit justify-start flex gap-2 items-center gray-400 col-span-3 pr-5"
          }
          onClick={() => router.push(`/profile/${card.author}`)}
        >
          <div
            className={
              "bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%]"
            }
          >
            {card.author.charAt(0).toUpperCase()}
          </div>
          <p className={"font-bold"}>@{card.author}</p>
        </button>
        {userIsAuthor ? (
          <button
            className={
              "w-fit h-fit p-1 px-2 text-white inline-block text-[80%] bg-red-400 rounded-full mr-2"
            }
            onClick={() => deleteCallback(body.id)}
          >
            Delete
          </button>
        ) : null}
      </div>
      <p className={`${cardFont}`}>&nbsp;&nbsp;&nbsp;&nbsp;{card.body}</p>
      <div
        className={"grid grid-cols-3 gap-5 transition-all duration-700 -mb-5"}
      >
        <div className={"border-t-2 w-full col-span-3"} />
        <button
          type={"button"}
          className={`w-fit h-11 rounded-full bg-gray-200 p-2 px-3 inline-flex items-center justify-center gap-2`}
          onClick={() => handleLikeClick()}
        >
          <img
            src={userLiked ? "/like.png" : "/like_empty.png"}
            className="w-4 text-gray-400"
            alt={""}
          />
          {card.likes}
        </button>
        <button
          type={"button"}
          className={`w-full h-11 rounded-full border-2 p-2 inline-flex items-center justify-center gap-2`}
          onClick={() => toggleComments()}
        >
          <img
            src={"/down-arrow.svg"}
            className={`${
              commentsOpened ? "scale-y-[-1]" : ""
            } w-4 text-gray-400`}
            alt={""}
          />
          Comments
        </button>
        <p className={"inline-flex items-center justify-end text-gray-500"}>
          {secondsToRelative(card.timestamp)}
        </p>
        <div
          ref={commentsContainerRef}
          className={
            "scrollbar-hidden col-span-3 transition-all duration-700 max-h-0 overflow-hidden opacity-0 grid gap-5 overflow-y-scroll border-t-2"
          }
        >
          <NewComment newCommentCallback={userComment} />
          {card.comments.map((c: any) => {
            return (
              <Comment body={c} key={c.id} deleteCallback={userCommentDelete} />
            );
          })}
        </div>
      </div>
    </div>
  );
}
