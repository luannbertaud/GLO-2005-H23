"use client";

export default function Comment() {
    return (
        <div  className={"h-fit w-full relative"}>
            <p className={"w-fit max-w-[80%] h-fit text-gray-600 font-semibold break-all inline-block"}>
                @Authorhyperlongdeoug:
            </p>
            <p className={"w-fit max-w-[20%] h-fit text-gray-400 break-all inline-block absolute right-0 text-[90%]"}>
                30sec ago
            </p>
            <p className={"w-fit max-w-full h-fit text-gray-600 break-all ml-3"}>
                Comment textComment textComment textComment text
            </p>
        </div>
    );
}