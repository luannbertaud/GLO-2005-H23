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
            if (r.ok) {
                setPosts(j);
                setLoading(false)
            }
        })).catch(e => {
            console.error(e);
        });
    }

    useEffect(() => {
        ValidateAccess(router, cookies["ipaper_user_token"]).then(() => {
            if (posts === undefined || posts.length === 0)
                loadPosts();
        });
    })
    if (loading) return <Loading/>;
    return (
        <div className="grid grid-row-1 gap-12 w-screen h-screen max-h-screen overflow-y-scroll items-center justify-center pt-5">
            <CitationCreator/>
            {
                posts.map((p : any)=> {
                    return <CitationCard body={p} key={p.id}/>
                })
            }
        </div>
    )
}
