"use client";

import {useState} from "react";
import {secondsToRelative} from "@/components/TimeParsing";

export default function Comment({ body } : any) {
    const [comment, setComment] : [any, any] = useState(body);

    return (
        <div  className={"h-fit w-full relative"}>
            <p className={"w-fit max-w-[80%] h-fit text-gray-600 font-semibold break-all inline-block"}>
                @{comment.author}:
            </p>
            <p className={"w-fit max-w-[20%] h-fit text-gray-400 break-all inline-block absolute right-0 text-[90%]"}>
                {secondsToRelative(comment.timestamp)}
            </p>
            <p className={"w-fit max-w-full h-fit text-gray-600 break-all ml-3"}>
                {comment.body}
            </p>
        </div>
    );
}