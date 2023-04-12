import styles from "../page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className="w-full -mt-10 font-mono">
        <div className="flex flex-row">
          <div className="bg-black rounded-full w-64 h-64 flex items-center justify-center mr-16">
            <span className="text-white text-9xl font-medium">U</span>
          </div>
          <div className="flex flex-row mr-10">
            <div className="flex flex-col justify-evenly">
              <p className="text-5xl font-semibold">
                Username
              </p>
              <p className="text-2xl">
                Biographie très très intéressante je vous le jure.
              </p>
            </div>
          </div>
          <div className="flex flex-row w-1/3 justify-center">
            <div className="flex flex-col justify-evenly">
              <div className="flex flex-row space-x-16 text-2xl font-semibold">
                <p>15 Following</p>
                <p>5 Followers</p>
                <p>42 Likes</p>
              </div>
              <div className="flex justify-center">
                  <button className="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 text-white text-2xl font-bold py-2 px-8 rounded">
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
