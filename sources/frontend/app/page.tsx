"use client";

import CitationCard from "@/components/CitationCard";
import CitationCreator from "@/components/CitationCreator";
import React, {useEffect, useState} from 'react';
import { ValidateAccess } from "@/components/Access";
import {useRouter} from "next/navigation";
import {useCookies} from "react-cookie";
import Loading from "@/app/loading";

export default function Feed() {
    const router = useRouter();
    const [cookies]: [any, any, any] = useCookies(['user']);
    const [loading, setLoading] = useState(true);
    const [posts, setPosts] = useState([]);

    async function userPostDelete(post_id : number) {
        console.log(post_id);
        let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/post`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
            body: JSON.stringify({
              "author": JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).username,
              "post_id": post_id,
            }),
          },
        });
  
        if (res.ok) {
            await res.text().then(_ => {
                loadPosts();
            })
        } else {
            await res.text().then(r => {
                alert(r);
            })
        }
    }

    async function loadPosts() {
        let token_id = "";
        if (cookies["ipaper_user_token"])
            token_id = JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id;
        fetch(`${process.env.NEXT_PUBLIC_API_HOST}/posts`, {
              method: 'GET',
              headers: {
                'X-token-id': token_id,
              },
        }).then(r => r.json().then(j => {
            setPosts(j);
            setLoading(false)
        })).catch(e => {
            console.error(e);
            setLoading(false);
        });
    }

    useEffect(() => {
        ValidateAccess(router, cookies["ipaper_user_token"]).then(() => {
            if (posts === undefined || posts.length === 0)
                loadPosts();
            else
                setLoading(false);
        });
    })
    if (loading) return <Loading/>;
    return (
        <div className="grid grid-row-1 gap-12 w-screen h-screen max-h-screen overflow-y-scroll items-center justify-center pt-5">
            <CitationCreator/>
            {
                posts.map((p : any)=> {
                    return <CitationCard body={p} key={p.id} deleteCallback={userPostDelete}/>
                })
            }
        </div>
    )
}
