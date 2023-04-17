"use client";

import React, { useState } from "react";
import { DynaPuff, Dancing_Script, Cinzel, Orbitron } from "next/font/google";
import {useCookies} from "react-cookie";
import {useRouter} from "next/navigation";

const dyna = DynaPuff({ subsets: ["latin"] });
const dancing = Dancing_Script({ subsets: ["latin"] });
const cinzel = Cinzel({ subsets: ["latin"] });
const orbit = Orbitron({ subsets: ["latin"] });

const FONT_FAMILIES = [
  [``, "Arial"],
  [`${dyna.className}`, "DynaPuff"],
  [`${dancing.className}`, "Dancing"],
  [`${cinzel.className}`, "Cinzel"],
  [`${orbit.className}`, "Orbitron"],
];

export default function QuoteCreator() {
  const router = useRouter();
  const [selectedFont, setSelectedFont] = useState("");
  const [quoteText, setQuoteText] = useState("");
  const [toggleSubmit, setToogleSubmit] = useState(false);
  const [timestamp, setTimestamp] = useState(new Date().toISOString().replace(/T/, ' ').replace(/\..+/, ''));
  const [cookies]: [any, any, any] = useCookies(['user']);

  async function postComment(data : any) {
    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/post`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
      },
      body: JSON.stringify({
        "author": data.author,
        "body": data.body,
        "police": data.police,
        "timestamp": data.timestamp,
      }),
    });
    if (res.ok) {
        res.text().then(j => {
            window.location.reload();
        })
    } else {
        res.json().then(j => {
            alert(j.desc);
        })
    }
}


  const handleFontChange = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setSelectedFont(event.target.value);
  };

  const handleQuoteChange = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setQuoteText(event.target.value);
    if (event.target.value != "")
      setToogleSubmit(true);
    else
      setToogleSubmit(false);
  };

  const handleSubmit = (event: { preventDefault: () => void }) => {
    event.preventDefault();
    setTimestamp(new Date().toISOString().replace(/T/, ' ').replace(/\..+/, ''));
    const policeName = FONT_FAMILIES.filter((e) => {
      if (e[0] === selectedFont) {
        return true
      }
      return false
    });
    const newQuote = {
      author: JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).username,
      body: quoteText,
      police: policeName[0][1],
      timestamp: timestamp
    };
    postComment(newQuote);
  };

  return (
    <div className="flex h-fit w-full max-w-2xl flex-col gap-5 rounded-2xl p-5 pt-7 font-mono shadow-2xl max-h-md">
      <form onSubmit={handleSubmit}>
        <label className="text-l font-semibold">Write your own quote!</label>
        <textarea
          id="quoteText"
          value={quoteText}
          onChange={handleQuoteChange}
          placeholder="Say what you want..."
          className={`${selectedFont} h-fit w-full my-3 rounded-lg border border-gray-200 flex-grow p-2`}
          rows={2}
        ></textarea>
        <div className="flex justify-between">
          <div>
            <label htmlFor="fontSelect">Choose a font:</label>
            <select
              id="font-family"
              className="mx-4 h-11 rounded-full border-2 p-2 inline-flex items-center justify-center gap-2"
              onChange={handleFontChange}
              value={selectedFont}
            >
              {FONT_FAMILIES.map((font) => (
                <option key={font[1]} value={font[0]}>
                  {font[1]}
                </option>
              ))}
            </select>
          </div>
          <button
            type="submit"
            disabled={!toggleSubmit}
            className={`${toggleSubmit ? "hover:bg-blue-700 cursor-pointer" : "disabled:opacity-75 cursor-not-allowed bg-gray-300"} bg-blue-500 text-white font-bold py-2 px-4 mx-4 h-12 rounded-full border-2 inline-flex items-center justify-center`}
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
