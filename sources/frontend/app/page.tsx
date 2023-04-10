import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "./page.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className={styles.main}>
      <div className="w-full -mt-10">
        <div className="flex flex-row">
          <div className="bg-black rounded-full w-64 h-64 flex items-center justify-center mr-16">
            <span className="text-white text-9xl font-medium">U</span>
          </div>
          <div className="flex flex-row mr-10">
            <div className="flex flex-col justify-evenly">
              <p className={`${styles.code} text-5xl font-semibold`}>
                Username
              </p>
              <p className={`${styles.code} text-2xl`}>
                Biographie très très intéressante je vous le jure.
              </p>
            </div>
          </div>
          <div className="flex flex-row w-1/3 justify-center">
            <div className="flex flex-col justify-evenly">
              <div className="flex flex-row space-x-16 text-2xl font-semibold">
                <p className={styles.code}>15 Following</p>
                <p className={styles.code}>5 Followers</p>
                <p className={styles.code}>42 Likes</p>
              </div>
              <div className="flex justify-center">
                  <button className={`${styles.code}, bg-blue-500 hover:bg-blue-600 active:bg-blue-700 text-white text-2xl font-bold py-2 px-8 rounded`}>
                    Follow
                  </button>
              </div>
            </div>
          </div>
        </div>
        <div className="border border-gray-300 my-10"></div>
        <div>
          oui bonjour
        </div>
      </div>
    </main>
  );
}
