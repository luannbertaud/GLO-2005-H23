"use client";

export async function ValidateAccess(router: any, cookieValue: string) {
    if (cookieValue === undefined || cookieValue === "") {
        await router.push("/authentification");
        return false;
    }

    let token_id = undefined;
    try {
        token_id = JSON.parse(Buffer.from(cookieValue, 'base64').toString('ascii')).token_id
    } catch (SyntaxError) {
        await router.push("/authentification");
    }

    let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/verify_token`, {
          method: 'GET',
          headers: {
            'X-token-id': token_id,
          },
    });

    if (!res.ok) {
        await router.push("/authentification");
        return false;
    }
    return true;
}

export async function RemoveAccess(remover: any, router: any, cookieValue : string) {
    await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/logout`, {
          method: 'POST',
          headers: {
            'X-token-id': JSON.parse(Buffer.from(cookieValue, 'base64').toString('ascii')).token_id,
          },
    });

    remover("ipaper_user_token")
    await router.push("/authentification");
}

export async function GrantAccess(setter: any, router: any, cookieValue : string) {
    setter("ipaper_user_token", cookieValue)
    await router.push("/");
}