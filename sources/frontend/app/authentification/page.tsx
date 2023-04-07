"use client";

import React from "react";

export default function Auth() {
    const [signup, setSignup] = React.useState(false);
    const [loading, setLoading] = React.useState(false);

    async function handleSubmit(event : any) {
        event.preventDefault();
        setLoading(true);
        setTimeout(() => {
            console.log(event.target.email.value + "   " + event.target.password.value);
            setLoading(false);
        }, 3000);
    }

    return (
        <div className="flex h-screen items-center justify-center">
            <div className="h-fit w-fit max-w-2xl rounded-2xl p-5 pt-3 shadow-2xl max-h-md flex flex-col font-mono">
                <img src={"/logo_rec.png"} className={"h-32"} alt={""}/>
                <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-5 text-lg grid-cols-[auto_minmax(0,_1fr)]">
                    <label htmlFor="email" className={"text-end m-auto mr-0"}>Email:</label>
                    <input type="text" id="email" className={"rounded-lg border border-gray-200 text-center py-1"}/>
                    <label htmlFor="password" className={"text-end m-auto mr-0"}>Password:</label>
                    <input type="password" id="password" className={"rounded-lg border border-gray-200 text-center py-1"}/>
                    <div/>
                    <button type="submit" className={`rounded-lg bg-gray-200 p-2 px-3 m-auto mr-0 flex gap-2 ${loading ? "opacity-50" : ""}`} disabled={loading} >
                        { loading ? <img src={"/oval.svg"} className="animate-spin w-6 text-gray-400" alt={""}/> : null}
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
}