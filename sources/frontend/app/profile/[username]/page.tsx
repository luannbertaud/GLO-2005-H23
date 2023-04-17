'use client';

import styles from "../../page.module.css";
import CitationCard from "@/components/CitationCard";
import React, {useEffect, useState} from "react";
import Loading from "@/app/loading";
import {useCookies} from "react-cookie";
import {useRouter} from "next/navigation";
import {ValidateAccess} from "@/components/Access";


export default function Profile({params} : any) {
    const [data, setData] : [any, any] = useState(undefined);
    const [posts, setPosts] : [any, any] = useState(undefined);
    const [cookies]: [any, any, any] = useCookies(['user']);
    const username = params.username;
    const router = useRouter();

    async function loadProfile() {
          await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/profile/${username}`, {
                method: 'GET',
                headers: {
                  'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
            },
          }).then(r => r.json().then(j => {
            if (r.ok)
                setData(j);
            else
                router.push('/');
          })).catch(e => {
              console.error(e);
              router.push('/');
          });
    }

    async function userPostDelete(post_id : number) {
      let res = await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/post/${post_id}`, {
        method: 'DELETE',
        headers: {
          'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
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
        await fetch(`${process.env.NEXT_PUBLIC_API_HOST}/posts/${username}`, {
                method: 'GET',
                headers: {
                'X-token-id': JSON.parse(Buffer.from(cookies["ipaper_user_token"], 'base64').toString('ascii')).token_id,
            },
        }).then(r => r.json().then(j => {
            if (r.ok)
                setPosts(j);
            else
                router.push('/');
        })).catch(e => {
            console.error(e);
            router.push('/');
        });
    }

    useEffect(() => {
        ValidateAccess(router, cookies["ipaper_user_token"]).then(() => {
            if (posts === undefined)
                loadPosts();
            if (data === undefined)
                loadProfile();
        });
    })

  if (data === undefined || posts === undefined) return <Loading/>;
  return (
    <main className={styles.main}>
      <div className="w-full -mt-10 font-mono">
        <div className="flex flex-row">
          <div className="bg-black rounded-full w-64 h-64 flex items-center justify-center mr-16">
            <span className="text-white text-9xl font-bold">{data.username.toUpperCase().charAt(0)}</span>
          </div>
          <div className="flex flex-row mr-10">
            <div className="flex flex-col justify-evenly">
              <p className="text-4xl font-semibold">
                  @{data.username}
              </p>
              <p className="text-xl">
                  {data.bio}
              </p>
            </div>
          </div>
          <div className="flex flex-row w-1/3 justify-center">
            <div className="flex flex-col justify-evenly">
              <div className="flex flex-row space-x-16 text-xl font-semibold">
                <p>{data.following} Following</p>
                <p>{data.followers} Followers</p>
                <p>{data.likes} Likes</p>
              </div>
              <div className="flex justify-center">
                  {/* <button className="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 text-white text-2xl font-bold py-2 px-8 rounded">
                    Follow
                  </button> */}
              </div>
            </div>
          </div>
        </div>
        <div className="border border-gray-300 my-10"></div>
        <div className="grid grid-cols-3 gap-12 w-full h-full overflow-y-scroll justify-center p-16">
            {
                posts.map((p : any)=> {
                    return <CitationCard body={p} key={p.id} deleteCallback={userPostDelete}/>
                })
            }
        </div>
      </div>
    </main>
  );
}
