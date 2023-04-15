"use client";

import React, { useState } from "react";
import { DynaPuff, Dancing_Script, Cinzel, Orbitron } from "next/font/google";

const dyna = DynaPuff({ subsets: ["latin"] });
const dancing = Dancing_Script({ subsets: ["latin"] });
const cinzel = Cinzel({ subsets: ["latin"] });
const orbit = Orbitron({ subsets: ["latin"] });

const FONT_FAMILIES = [
  [undefined, "Arial"],
  [`${dyna.className}`, "DynaPuff"],
  [`${dancing.className}`, "Dancing"],
  [`${cinzel.className}`, "Cinzel"],
  [`${orbit.className}`, "Orbitron"],
];

export default function QuoteCreator() {
  const [selectedFont, setSelectedFont] = useState("Arial");
  const [quoteText, setQuoteText] = useState("");
  const [timestamp, setTimestamp] = useState(new Date().getTime() / 1000);

  const handleFontChange = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setSelectedFont(event.target.value);
  };

  const handleQuoteChange = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setQuoteText(event.target.value);
  };

  const handleSubmit = (event: { preventDefault: () => void }) => {
    event.preventDefault();
    const newQuote = {
      body: quoteText,
      timestamp: timestamp,
    };
    console.log("Submitting quote: ", newQuote);
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
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-4 h-12 rounded-full border-2 inline-flex items-center justify-center"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
