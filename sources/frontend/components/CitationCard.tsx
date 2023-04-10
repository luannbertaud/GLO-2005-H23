'use client';

import React from "react";

export default function CitationCard() {
    const [userLiked, setUserLiked] = React.useState(false);
    const [commentsOpened, setCommentsOpened] = React.useState(false);
    const commentsContainerRef = React.createRef<HTMLDivElement>();

    async function toggleComments() {
        const commentsContainer = commentsContainerRef.current;
        const commentsContainerForm = commentsContainer!.parentElement;
        if (!commentsOpened) {
            commentsContainer!.style.marginBottom = "1.25rem";
            commentsContainer!.style.maxHeight = "500px";
            setTimeout(() => {
                commentsContainer!.style.opacity = "1";
            }, 400);
        } else {
            commentsContainer!.style.opacity = "0";
            setTimeout(() => {
                commentsContainer!.style.maxHeight = "0";
                commentsContainer!.style.marginBottom = "-1.25rem";
            }, 400);
        }
        setCommentsOpened(!commentsOpened);
    }

    return (
        <div className="flex h-fit w-fit max-w-2xl flex-col gap-5 rounded-2xl p-5 font-mono shadow-2xl max-h-md">
            <p>{"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."}</p>
            <div className={"border-t-2 w-full"}></div>
            <div className={"grid grid-cols-3 gap-5 transition-all duration-700 -mb-5"}>
                <button type={"button"} className={`w-fit h-11 rounded-full bg-gray-200 p-2 px-3 inline-flex items-center justify-center gap-2`} onClick={() => setUserLiked(!userLiked)}>
                    <img src={userLiked ? "/like.png" : "/like_empty.png"} className="w-4 text-gray-400" alt={""}/>
                    100
                </button>
                <button type={"button"} className={`w-full h-11 rounded-full border-2 p-2 inline-flex items-center justify-center gap-2`} onClick={() => toggleComments()}>
                    <img src={"/down-arrow.svg"} className="w-4 text-gray-400" alt={""}/>
                    Comments
                </button>
                <p className={"inline-flex items-center justify-end text-gray-500"}>10m ago</p>
                <div ref={commentsContainerRef} className={"col-span-3 transition-all duration-700 max-h-0 overflow-hidden opacity-0"}>
                    <div className={"min-h-[150px] bg-red-700"}></div>
                </div>
            </div>
        </div>
    );
}