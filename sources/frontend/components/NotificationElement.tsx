"use client";

import { secondsToRelative } from "./TimeParsing";

type notifProps = {
  body: any
};

export default function Notification({ body }: notifProps) {

  return (
    <div className={"w-full relative"}>
      <div className="flex items-start px-ype originates at this import.4 py-3">
        <div className="flex-shrink-0 mr-3">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            className="bi bi-chat"
            viewBox="0 0 16 16"
          >
            {" "}
            <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z" />{" "}
          </svg>
        </div>
        <div className="flex-grow">
          <div className="font-medium text-sm text-gray-900">
            { body[4] === "like" ? `${body[1]} à aimé votre citation` : null}
            { body[4] === "comment" ? `${body[1]} à commenté votre citation` : null}
            { body[4] === "follow" ? `${body[1]} à commencé à vous suivre` : null}
          </div>
          <div className="mt-1 text-sm text-gray-500">{secondsToRelative((Date.parse(body[2])) / 1000 )}</div>
        </div>
      </div>
    </div>
  );
}
