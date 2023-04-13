'use client';

import React, {useEffect, useState} from "react";
import Comment from "@/components/Comment";
import NewComment from "@/components/NewComment";
import {secondsToRelative} from "@/components/TimeParsing";
import Loading from "@/app/loading";

async function loadCitationCard(id :string) {
    await new Promise(r => setTimeout(r, 200));
    // let res = await fetch("");
    let post = {
        "author": "Tom",
        "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
        "timestamp": 983646381,
        "police": "",
        "likes": 108,
        "userLike": false,
        "comments": [
            1, 2, 3, 4
        ]
    };
    return {...post, "timestamp": secondsToRelative(post.timestamp)};
}

export default function CitationCard({ body } : any) {
    const [userLiked, setUserLiked] = React.useState(false);
    const [commentsOpened, setCommentsOpened] = React.useState(false);
    const [card, setCard] : [any, any] = useState(body);
    const commentsContainerRef = React.createRef<HTMLDivElement>();

    // useEffect(() => {
    //     if (card === undefined)
    //         loadCitationCard(id).then((c) => {
    //             setUserLiked(c.userLike);
    //             setCard(c);
    //         });
    // })
    // if (card === undefined) return <Loading/>;

    async function userLike() {
        await new Promise(r => setTimeout(r, 500));
        setUserLiked(true);
        // loadCitationCard(id).then((c) => {
        //     setCard({...c, "likes": c.likes+1});
        // });
    }

    async function userComment(content : string) {
        console.log(content)
        await new Promise(r => setTimeout(r, 500));
        // loadCitationCard(id).then((c) => {
        //     setCard({...c, "comments": [...c.comments, 8]});
        // });
    }

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
        <div className="flex h-fit w-fit max-w-2xl flex-col gap-5 rounded-2xl p-5 pt-7 font-mono shadow-2xl max-h-md">
            <div className={"w-full justify-start flex gap-2 items-center gray-400 col-span-3 pr-5"}>
                <div className={"bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%]"}>{card.author.charAt(0).toUpperCase()}</div>
                <p className={"font-bold"}>@{card.author}</p>
            </div>
            <p>&nbsp;&nbsp;&nbsp;&nbsp;{card.body}</p>
            <div className={"grid grid-cols-3 gap-5 transition-all duration-700 -mb-5"}>
                <div className={"border-t-2 w-full col-span-3"}/>
                <button type={"button"} className={`w-fit h-11 rounded-full bg-gray-200 p-2 px-3 inline-flex items-center justify-center gap-2`} onClick={() => userLike()}>
                    <img src={userLiked ? "/like.png" : "/like_empty.png"} className="w-4 text-gray-400" alt={""}/>
                    {card.likes}
                </button>
                <button type={"button"} className={`w-full h-11 rounded-full border-2 p-2 inline-flex items-center justify-center gap-2`} onClick={() => toggleComments()}>
                    <img src={"/down-arrow.svg"} className={`${commentsOpened ? "scale-y-[-1]" : ""} w-4 text-gray-400`} alt={""}/>
                    Comments
                </button>
                <p className={"inline-flex items-center justify-end text-gray-500"}>{secondsToRelative(card.timestamp)}</p>
                <div ref={commentsContainerRef} className={"scrollbar-hidden col-span-3 transition-all duration-700 max-h-0 overflow-hidden opacity-0 grid gap-5 overflow-y-scroll border-t-2"}>
                    <NewComment newCommentCallback={userComment}/>
                     {/*{*/}
                     {/*    card.comments.map((cId : any, index : number)=> {*/}
                     {/*       return <Comment id={cId} key={index}/>*/}
                     {/*   })*/}
                     {/*}*/}
                </div>
            </div>
        </div>
    );
}