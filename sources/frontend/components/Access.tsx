"use client";

/**
 * Ensures that the user has a valid token.
 *
 * @param router - Used to redirect the user if the acces is denied
 * @param cookieValue - Contains the logged-in user's token
 *
 * @returns - True if the user has a valid token, false if not.
 */

export async function ValidateAccess(router: any, cookieValue: string) {
  if (cookieValue === undefined || cookieValue === "") {
    await router.push("/authentification");
    return false;
  }

  let token_id = undefined;
  try {
    token_id = JSON.parse(
      Buffer.from(cookieValue, "base64").toString("ascii")
    ).token_id;
  } catch (SyntaxError) {
    await router.push("/authentification");
  }

  let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/verify_token`, {
    method: "GET",
    headers: {
      "X-token-id": token_id,
    },
  });

  if (!res.ok) {
    await router.push("/authentification");
    return false;
  }
  return true;
}

/**
 * Removes stored token when the user is logging out and redirects him to the login page.
 *
 * @param remover - Used to remove the stored token
 * @param router - Used to redirect the user if the acces is denied
 * @param cookieValue - Contains the logged-in user's token
 */

export async function RemoveAccess(
  remover: any,
  router: any,
  cookieValue: string
) {
  await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/logout`, {
    method: "POST",
    headers: {
      "X-token-id": JSON.parse(
        Buffer.from(cookieValue, "base64").toString("ascii")
      ).token_id,
    },
  });

  remover("ipaper_user_token");
  await router.push("/authentification");
}

/**
 * Stores the user's token in the cookies and redirects him to the Home page.
 *
 * @param setter - Used to store the user's token
 * @param router - Used to redirect the user if the acces is denied
 * @param cookieValue - Contains the logged-in user's token
 */

export async function GrantAccess(
  setter: any,
  router: any,
  cookieValue: string
) {
  setter("ipaper_user_token", cookieValue);
  await router.push("/");
}
