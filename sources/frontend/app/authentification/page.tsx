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

    async function toggleSignup() {
        let elements : string[] = ["firstname", "firstname-l", "lastname", "lastname-l", "username", "username-l", "bio", "bio-l"];

        if (!signup) {
            document.getElementById("signup-container")!.style.maxHeight = "500px";
            setTimeout(() => {
                for (let i = 0; i < elements.length; i++) {
                    document.getElementById(elements[i])!.style.opacity = "1";
                }
            }, 200);
        } else {
            for (let i = 0; i < elements.length; i++) {
                document.getElementById(elements[i])!.style.opacity = "0";
            }
            setTimeout(() => {
                document.getElementById("signup-container")!.style.maxHeight = "0px";
            }, 200);
        }
        setSignup(!signup);
    }

    return (
        <div className="flex h-screen items-center justify-center">
            <div className="flex h-fit w-fit max-w-2xl flex-col rounded-2xl p-5 pt-3 font-mono shadow-2xl max-h-md">
                <img src={"/logo_rec.png"} className={"h-32"} alt={""}/>
                <form onSubmit={handleSubmit} className="grid grid-cols-2 h-fit gap-5 text-lg grid-cols-[auto_minmax(0,_1fr)]">
                    <label htmlFor="email" className={"text-end m-auto mr-0"}>Email:</label>
                    <input type="text" id="email" className={"rounded-lg border border-gray-200 text-center py-1"}/>
                    <label htmlFor="password" className={"text-end m-auto mr-0"}>Password:</label>
                    <input type="password" id="password" className={"rounded-lg border border-gray-200 text-center py-1"}/>

                    <div id={"signup-container"} className="grid-cols-2 h-fit gap-5 text-lg grid-cols-[auto_minmax(0,_1fr)] transition-all duration-500 col-span-2 max-h-0 grid overflow-hidden">
                        <label htmlFor="firstname" id="firstname-l" className={"text-end m-auto transition-all duration-500 mr-0 opacity-0"}>Firstname:</label>
                        <input type="text" id="firstname" className={"rounded-lg transition-all duration-500 border border-gray-200 text-center py-1 opacity-0"}/>
                        <label htmlFor="lastname" id="lastname-l" className={"text-end m-auto mr-0 opacity-0 transition-all duration-500"}>Lastname:</label>
                        <input type="text" id="lastname" className={"rounded-lg border border-gray-200 text-center py-1 opacity-0 transition-all duration-500"}/>
                        <label htmlFor="username" id="username-l" className={"text-end m-auto mr-0 opacity-0 transition-all duration-500"}>Username:</label>
                        <input type="text" id="username" className={"rounded-lg border border-gray-200 text-center py-1 opacity-0 transition-all duration-500"}/>
                        <label htmlFor="bio" id="bio-l" className={"text-end m-auto mr-0 opacity-0 transition-all duration-500"}>Bio:</label>
                        <textarea id="bio" className={"rounded-lg border border-gray-200 text-center py-1 opacity-0 transition-all duration-500"} rows={2}/>
                    </div>

                    <button type={"button"} className={`w-28 rounded-lg bg-gray-200 p-2 px-3 m-auto mr-0 inline-flex items-center justify-center gap-2 ${loading ? "opacity-50" : ""}`} onClick={() => toggleSignup()}>
                        <img src={"/replace.svg"} className="w-4 text-gray-400" alt={""}/>
                        { signup ? "Login" : "Signup" }
                    </button>
                    <button type={"submit"} className={`min-w-28 rounded-lg bg-gray-200 p-2 px-3 m-auto mr-0 inline-flex items-center justify-center gap-2 ${loading ? "opacity-50" : ""}`} disabled={loading} >
                        { loading ? <img src={"/oval.svg"} className="w-6 animate-spin text-gray-400" alt={""}/> : null}
                        { signup ? "Signup" : "Login" }
                        <img src={"/arrow_right.svg"} className="w-4 text-gray-400" alt={""}/>
                    </button>
                </form>
            </div>
        </div>
    );
}