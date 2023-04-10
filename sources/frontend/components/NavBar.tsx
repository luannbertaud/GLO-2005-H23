"use client";

import React from "react";
import Link from "next/link";
export default function NavBar() {
    return (
        <div className={"w-full h-20 border-b-2 flex flex-row p-4 justify-center items-center gap-6 relative"}>
            <Link href={"/"} className={`w-fit h-full absolute left-0 inline-flex items-center justify-center`}>
                    <img src={"/logo_rec.png"} className={"h-full"} alt={""}/>
            </Link>
            <span className={"flex-grow"}></span>
            <div className={"flex justify-center items-center"}>
                <input type={"text"} className={`w-fit h-11 rounded-l-full border-2 border-r-0 outline-none p-2 px-4`}/>
                <button className={`w-fit h-11 rounded-r-full border-2 border-l-0 bg-gray-200 p-2 px-3 inline-flex items-center justify-center`}>
                    <img src={"/search.png"} className={"w-5 text-gray-400"} alt={""}/>
                </button>
            </div>
            <button className={`w-fit h-11 rounded-full border-2 p-2 px-4 inline-flex items-center justify-center gap-2`}>
                <img src={"/write.svg"} className={"w-4 text-gray-400"} alt={""}/>
                New Post
            </button>
            <button className={`w-fit h-11 rounded-full border-2 p-2 px-2 inline-flex items-center justify-center`}>
                <img src={"/notification.png"} className={"w-6 opacity-80"} alt={""}/>
            </button>
            <Link href={"/profile"} className={"bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%]"}>U</Link>
        </div>
    );
}