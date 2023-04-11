import './globals.css'
import React from "react";
import NavBar from "@/components/NavBar";

export const metadata = {
  title: 'InstaPaper',
  description: '',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {

  return (
    <html lang="fr">
      <body>
        <NavBar/>
        {children}
      </body>
    </html>
  )
}
