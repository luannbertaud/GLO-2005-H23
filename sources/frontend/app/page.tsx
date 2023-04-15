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
        fetch(`${process.env.NEXT_PUBLIC_API_HOST}/posts`, {
              method: 'GET',
              headers: {
                'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
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
                 posts.map((p : any, index : number)=> {
                    return <CitationCard body={p} key={index}/>
                })
             }
        </div>
    )
}
