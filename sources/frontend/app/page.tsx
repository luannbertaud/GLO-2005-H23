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
    const [pagination, setPagination] = useState([0, 10]);
    let debounceScroll = Date.now();

    async function loadPosts(forced_pagination: any = undefined, addToCurrent: boolean = false) {
        let pa = forced_pagination;
        if (pa === undefined)
            pa = pagination;
        let token_id = "";
        if (cookies["ipaper_user_token"])
            token_id = JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id;
        fetch(`${process.env.NEXT_PUBLIC_API_HOST}/posts?page=${pa[0]}&page_size=${pa[1]}`, {
              method: 'GET',
              headers: {
                'X-token-id': token_id,
              },
        }).then(r => r.json().then(j => {
            if (r.ok) {
                if (addToCurrent)
                    j = [...posts, ...j];
                setPosts(j);
                setLoading(false);
            }
        })).catch(e => {
            console.error(e);
        });
    }

    async function scrollHandling(e : any) {
        e.preventDefault()
        if (Date.now() - debounceScroll > 1000 && e.target.offsetHeight + e.target.scrollTop >= e.target.scrollHeight) {
            debounceScroll = Date.now();
            loadPosts([pagination[0] + 1, pagination[1]], true).then(
                () => setPagination([pagination[0] + 1, pagination[1]])
            );
        }
    }

    useEffect(() => {
        ValidateAccess(router, cookies["ipaper_user_token"]).then(() => {
            if (posts === undefined || posts.length === 0)
                loadPosts();
        });
    })
    if (loading) return <Loading/>;
    return (
        <div className="grid grid-row-1 gap-12 w-screen h-screen max-h-screen overflow-y-scroll items-center justify-center pt-5"
            onScroll={(e) => scrollHandling(e)}>
            <CitationCreator/>
            {
                posts.map((p : any)=> {
                    return <CitationCard body={p} key={p.id}/>
                })
            }
        </div>
    )
}
