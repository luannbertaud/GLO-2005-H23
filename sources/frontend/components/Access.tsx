"use client";

export async function ValidateAccess(router: any, cookieValue: string) {
    if (cookieValue === undefined || cookieValue === "")
        await router.push("/authentification");

    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/verify_token`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-token-id': JSON.parse(decodeURIComponent(cookieValue)).token_id,
          },
        });

    if (!res.ok)
        await router.push("/authentification");
}

export async function RemoveAccess(remover: any, router: any) {
    remover("ipaper_user_token")
    await router.push("/authentification");
}

export async function GrantAccess(setter: any, router: any, cookieValue : string) {
    setter("ipaper_user_token", cookieValue)
    await router.push("/");
}