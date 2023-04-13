"use client";

import CitationCard from "@/components/CitationCard";
import {useEffect, useState} from 'react';
import { ValidateAccess } from "@/components/Access";
import {useRouter} from "next/navigation";
import {useCookies} from "react-cookie";
import Loading from "@/app/loading";

export default function Feed() {
    const router = useRouter();
    const [cookies]: [any, any, any] = useCookies(['user']);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        ValidateAccess(router, cookies["ipaper_user_token"]).then(() => setLoading(false));
    })
    if (loading) return <Loading/>;
    return (
        <div className="grid grid-row-1 gap-12 w-screen h-screen max-h-screen overflow-y-scroll items-center justify-center pt-5">
            <CitationCard/>
            <CitationCard/>
            <CitationCard/>
            <CitationCard/>
            <CitationCard/>
        </div>
    )
}
