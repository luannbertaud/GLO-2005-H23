"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { Popover } from "@varld/popover";
import Notification from "@/components/NotificationElement";
import { RemoveAccess } from "@/components/Access";
import { useRouter } from "next/navigation";
import { useCookies } from "react-cookie";

export default function NavBar() {
  const [suggestions, setSuggestions] = useState([]);
  const [notificationsData, setNotificationsData] = useState([]);
  const [menuOpened, setMenuOpened] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [showBadge, setShowBadge] = useState(false);
  const router = useRouter();
  const [cookies, __, removeCookie]: [any, any, any] = useCookies(["user"]);

  useEffect(() => {
    getNotifications();
  }, []);

  let username = "";
  if (cookies["ipaper_user_token"] !== undefined)
    username = JSON.parse(
      Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
    ).username;

  function toggleMenu(value: any) {
    const menu = document.getElementById("menu");
    if (value === undefined) value = !menuOpened;
    if (!value) menu!.style.maxHeight = "0";
    else menu!.style.maxHeight = "100px";
    setMenuOpened(!menuOpened);
  }

  async function getNotifications() {
    await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/notifs`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
    })
      .then((r) => {
        r.json().then((j) => {
          if (r.ok) {
            if (j.length == 0) {
              return [];
            }
            j.sort((a: (string | number | Date)[], b: (string | number | Date)[]) => new Date(b[2]).valueOf() - new Date(a[2]).valueOf());
            setNotificationsData(j);
            if (j[0][3] === "unread") {
              setShowBadge(true);
            }
          } else router.push("/");
        });
      })
      .catch((e) => {
        console.error(e);
        router.push("/");
      });
  }

  async function readNotifications() {
    await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/notifs`, {
      method: "PATCH",
      headers: {
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
    })
      .then((r) => {
        r.text().then((j) => {
          if (r.ok) {
            setShowBadge(false);
          }
        }).catch(() => {
          router.push("/");
        });
      })
      .catch((e) => {
        console.error(e);
        router.push("/");
      });
  }

  async function loadSuggestions(event: any) {
    const input = event.currentTarget.value;
    if (input == "") {
      setShowSuggestions(false);
      return;
    }
    await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/search/${input}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-token-id": JSON.parse(
          Buffer.from(cookies["ipaper_user_token"], "base64").toString("ascii")
        ).token_id,
      },
    })
      .then((r) => {
        r.json().then((j) => {
          if (r.ok) {
            setSuggestions(j.slice(0, 5));
          } else router.push("/");
        });
      })
      .catch((e) => {
        console.error(e);
        router.push("/");
      });
  }

  async function logout() {
    await RemoveAccess(removeCookie, router, cookies["ipaper_user_token"]).then(
      () => {
        toggleMenu(false);
      }
    );
  }

  return (
    <div
      className={
        "w-full h-20 border-b-2 flex flex-row p-4 justify-center items-center gap-6 relative"
      }
    >
      <Link
        href={"/"}
        className={`w-fit h-full absolute left-0 inline-flex items-center justify-center`}
      >
        <img src={"/logo_rec.png"} className={"h-full"} alt={""} />
      </Link>
      <span className={"flex-grow"}></span>
      <div className={"flex justify-center items-center"}>
        <div className="relative">
          <input
            type={"text"}
            placeholder="Search a user..."
            onChange={loadSuggestions}
            onFocus={(e) => {
              setShowSuggestions(true);
            }}
            onBlur={(e) => {
              setTimeout(() => setShowSuggestions(false), 200);
            }}
            className={`w-fit h-11 rounded-full border-2 outline-none p-2 pl-8 px-4`}
          />
          <svg
            className="w-4 h-4 absolute left-2.5 top-3.5"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
          <div
            id="suggestionContainer"
            className={`${
              showSuggestions ? "visible" : "invisible"
            } absolute mt-2 w-full overflow-hidden rounded-md bg-white`}
          >
            {suggestions.map((e: any, i) => (
              <div
                onClick={() => router.push(`/profile/${e.username}`)}
                className="cursor-pointer py-2 px-3 hover:bg-slate-100"
                key={i}
              >
                <p className="text-sm font-medium text-gray-600">
                  {e.username}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
      <button
        className={`w-fit h-11 rounded-full border-2 p-2 px-4 inline-flex items-center justify-center gap-2 hover:bg-gray-100 active:bg-gray-200`}
        onClick={() => {
          router.push("/");
        }}
      >
        <img src={"/write.svg"} className={"w-4 text-gray-400"} alt={""} />
        New Post
      </button>
      <Popover
        popover={() => {
          return (
            <div className="popover divide-y divide-gray-200">
              <h5 className="font-medium">Notifications</h5>
              {notificationsData.map((e, i) => (
                <Notification body={e} key={i} />
              ))}
            </div>
          );
        }}
      >
        <button
          onClick={() => {
            readNotifications();
          }}
          className={`w-fit h-11 rounded-full border-2 p-2 px-2 inline-flex items-center justify-center relative hover:bg-gray-100 active:bg-gray-200`}
        >
          <img
            src={"/notification.png"}
            className={"w-6 opacity-80"}
            alt={""}
          />
          <span
            className={`${
              showBadge ? "visible" : "invisible"
            } top-0 left-7 absolute  w-3.5 h-3.5 bg-red-500 border-2 border-white rounded-full`}
          ></span>
        </button>
      </Popover>
      <button
        className={
          "bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%] relative"
        }
        onClick={() => toggleMenu(undefined)}
      >
        <img src={"/profile.png"} className={"w-6"} alt={"profile"} />
      </button>
      <div
        id="menu"
        className={
          "absolute w-fit h-fit top-full right-0 text-gray-500 mr-5 mt-2 grid grid-cols-1 gap-1 max-h-0 transition-all duration-500 overflow-hidden"
        }
      >
        <button
          className={"text-[180%]"}
          onClick={() => {
            toggleMenu(false);
            router.push(`/profile/${username}`);
          }}
        >
          Profile
        </button>
        <div className={"border-t-2 w-full"} />
        <button className={"text-[180%]"} onClick={() => logout()}>
          Logout
        </button>
      </div>
    </div>
  );
}
