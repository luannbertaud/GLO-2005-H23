"use client";

import { useRouter } from "next/navigation";
import { useCookies } from "react-cookie";

export async function ValidateAccess(router: any, cookieValue: string) {
    await new Promise(r => setTimeout(r, 500));
    if (cookieValue !== "a")
        router.push("/authentification");
}

export async function RemoveAccess(remover: any, router: any) {
    remover("ipaper_user_token")
    router.push("/authentification");
}

export async function GrantAccess(setter: any, router: any, cookieValue : string) {
    await new Promise(r => setTimeout(r, 2000));
    setter("ipaper_user_token", cookieValue)
    router.push("/");
}