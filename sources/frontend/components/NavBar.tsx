"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Popover } from "@varld/popover";
import Notification from "@/components/NotificationElement"
import { RemoveAccess } from "@/components/Access";
import { useRouter } from "next/navigation";
import { useCookies } from "react-cookie";
export default function NavBar() {
  const [menuOpened, setMenuOpened] = useState(false);
  const router = useRouter();
  const [cookies, __, removeCookie]: [any, any, any] = useCookies(["user"]);

  function toggleMenu(value: any) {
    const menu = document.getElementById("menu");
    if (value === undefined) value = !menuOpened;
    if (!value) menu!.style.maxHeight = "0";
    else menu!.style.maxHeight = "100px";
    setMenuOpened(!menuOpened);
  }

  function logout() {
    RemoveAccess(removeCookie, router, cookies["ipaper_user_token"]).then(() => {
      toggleMenu(false);
    });
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
        <input
          type={"text"}
          className={`w-fit h-11 rounded-l-full border-2 border-r-0 outline-none p-2 px-4`}
        />
        <button
          className={`w-fit h-11 rounded-r-full border-2 border-l-0 bg-gray-200 p-2 px-3 inline-flex items-center justify-center`}
        >
          <img src={"/search.png"} className={"w-5 text-gray-400"} alt={""} />
        </button>
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
        popover={( ) => {
          return (
            <div className="popover divide-y divide-gray-200">
              <h5 className="font-medium">Notifications</h5>
                {[...Array(5)].map((e, i) => <Notification className="busterCards" key={i}/>)}
            </div>
          );
        }}
      >
        <button
          className={`w-fit h-11 rounded-full border-2 p-2 px-2 inline-flex items-center justify-center relative hover:bg-gray-100 active:bg-gray-200`}
        >
          <img
            src={"/notification.png"}
            className={"w-6 opacity-80"}
            alt={""}
          />
          <span className="top-0 left-7 absolute  w-3.5 h-3.5 bg-red-500 border-2 border-white rounded-full"></span>
        </button>
      </Popover>
      <button
        className={
          "bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%] relative"
        }
        onClick={() => toggleMenu(undefined)}
      >
        U
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
            router.push("/profile");
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
