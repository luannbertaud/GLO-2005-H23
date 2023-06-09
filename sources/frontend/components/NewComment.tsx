"use client";

import React from "react";
import {useCookies} from "react-cookie";

export default function NewComment({ newCommentCallback } : any) {
    const [cookies]: [any, any, any] = useCookies(['user']);
    const commentBodyRef = React.createRef<HTMLTextAreaElement>();

    /**
    * Listener for the New comment Callback
    */

    async function handleNewComment() {
        if (commentBodyRef.current && commentBodyRef.current.value) {
            await newCommentCallback(commentBodyRef.current.value);
            commentBodyRef.current.value = "";
        }
    }

    return (
        <div  className={"h-fit w-full flex gap-3 mb-3 flex-wrap"}>
            <p className={"w-fit max-w-full h-fit text-gray-600 font-semibold break-all inline-block float-left"}>
                @{JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).username} :
            </p>
            <textarea ref={commentBodyRef} className={"h-fit rounded-lg border border-gray-200 flex-grow p-2"} rows={2}/>
            <div className={"w-full h-fit inline-flex items-center justify-end"}>
                <button type={"button"} className={`w-fit h-full rounded-full border-2 p-1 px-2 inline-flex items-center justify-center gap-2 text-[80%]`} onClick={() => handleNewComment()}>
                    <img src={"/comment.png"} className="w-3 text-gray-400" alt={""}/>
                    Add comment
                </button>
            </div>
        </div>
    );
}