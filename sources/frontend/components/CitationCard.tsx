'use client';

import React from "react";
import Comment from "@/components/Comment";

export default function CitationCard() {
    const [userLiked, setUserLiked] = React.useState(false);
    const [commentsOpened, setCommentsOpened] = React.useState(false);
    const commentsContainerRef = React.createRef<HTMLDivElement>();

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
        <div className="flex h-fit w-fit max-w-2xl flex-col gap-5 rounded-2xl p-5 py-7 font-mono shadow-2xl max-h-md">
            <p>&nbsp;&nbsp;&nbsp;&nbsp;{"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."}</p>
            <div className={"grid grid-cols-3 gap-5 transition-all duration-700 -mb-5"}>
                <div className={"flex justify-center items-center col-span-3 grid grid-cols-2"}>
                    <div className={"w-full flex gap-2 items-center gray-400"}>
                        <div className={"bg-gray-800 rounded-full w-12 h-12 text-white justify-center flex items-center font-bold text-[110%]"}>U</div>
                        <p className={"font-bold"}>@User</p>
                    </div>
                    <div className={"w-full flex justify-end"}>
                        <button type={"button"} className={`w-fit h-11 rounded-full border-2 p-4 inline-flex items-center justify-center gap-2`} onClick={() => toggleComments()}>
                            <img src={"/comment.png"} className="w-4 text-gray-400" alt={""}/>
                            Add comment
                        </button>
                    </div>
                </div>
                <div className={"border-t-2 w-full col-span-3"}/>
                <button type={"button"} className={`w-fit h-11 rounded-full bg-gray-200 p-2 px-3 inline-flex items-center justify-center gap-2`} onClick={() => setUserLiked(!userLiked)}>
                    <img src={userLiked ? "/like.png" : "/like_empty.png"} className="w-4 text-gray-400" alt={""}/>
                    100
                </button>
                <button type={"button"} className={`w-full h-11 rounded-full border-2 p-2 inline-flex items-center justify-center gap-2`} onClick={() => toggleComments()}>
                    <img src={"/down-arrow.svg"} className={`${commentsOpened ? "scale-y-[-1]" : ""} w-4 text-gray-400`} alt={""}/>
                    Comments
                </button>
                <p className={"inline-flex items-center justify-end text-gray-500"}>10m ago</p>
                <div ref={commentsContainerRef} className={"col-span-3 transition-all duration-700 max-h-0 overflow-hidden opacity-0 grid gap-5 overflow-y-scroll"}>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                    <Comment/>
                </div>
            </div>
        </div>
    );
}