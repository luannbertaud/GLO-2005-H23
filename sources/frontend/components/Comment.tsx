"use client";

import {useEffect, useState} from "react";
import {secondsToRelative} from "@/components/TimeParsing";
import {useCookies} from "react-cookie";
import Link from "next/link";

export default function Comment({ body, deleteCallback } : any) {
    const [comment] : [any, any] = useState(body);
    const [userIsAuthor, setUserIsAuthor]: [boolean, any] = useState(false);
    const [cookies]: [any, any, any] = useCookies(['user']);

    useEffect(() => {
        if (JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).username === body.author)
            setUserIsAuthor(true);
    }, [cookies, body.author])

    return (
        <div  className={"h-fit w-full relative"}>
            <div className={"w-full h-fit flex items-center"}>
                <Link className={"w-fit max-w-[80%] h-fit text-gray-600 font-semibold break-all inline-block"} href={`profile/${comment.author}`}>
                    @{comment.author}:
                </Link>
                <div className={"flex-grow"}/>
                {
                    userIsAuthor
                    ? <button className={"w-fit h-fit p-1 px-2 text-white inline-block text-[80%] bg-red-400 rounded-full mr-2"} onClick={() => deleteCallback(body.id)}>
                        Delete
                    </button>
                    : null
                }
                <div className={"w-fit h-fit text-gray-400 break-all inline-block text-[90%]"}>
                    {secondsToRelative(comment.timestamp)}
                </div>
            </div>
            <p className={"w-fit max-w-full h-fit text-gray-600 break-all ml-3"}>
                {comment.body}
            </p>
        </div>
    );
}