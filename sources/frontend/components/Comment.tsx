"use client";

import {useEffect, useState} from "react";
import {secondsToRelative} from "@/components/TimeParsing";
import Loading from "@/app/loading";

async function loadComment(id :string) {
    await new Promise(r => setTimeout(r, 2000));
    // let res = await fetch("");
    let post = {
        "author": "Johnny",
        "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
        "timestamp": 983446381,
    };
    return {...post, "timestamp": secondsToRelative(post.timestamp)};
}


export default function Comment({ id } : any) {
    const [post, setPost] : [any, any] = useState(undefined);

    useEffect(() => {
         if (post === undefined)
            loadComment(id).then((p) => setPost(p));
    })
    if (post === undefined) return <Loading/>;
    return (
        <div  className={"h-fit w-full relative"}>
            <p className={"w-fit max-w-[80%] h-fit text-gray-600 font-semibold break-all inline-block"}>
                @{post.author}:
            </p>
            <p className={"w-fit max-w-[20%] h-fit text-gray-400 break-all inline-block absolute right-0 text-[90%]"}>
                {post.timestamp}
            </p>
            <p className={"w-fit max-w-full h-fit text-gray-600 break-all ml-3"}>
                {post.body}
            </p>
        </div>
    );
}