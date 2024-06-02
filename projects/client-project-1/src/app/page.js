import Image from "next/image";
import Head from "next/head";
import Hero from "./components/Hero";

export default function Home() {
  return (
    <>
      <Head>
        <title>Sacred Spirituality</title>
        <meta name="description" content="Unlock transformation. Book an appointment at Sacred Spirituality to unveil Reiki's healing power, seek energy work, and experience quality spiritual guidance." />
      </Head>
      <main>
        <Hero />
      </main>
    </>
  );
}
