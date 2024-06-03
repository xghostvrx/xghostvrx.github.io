import Head from "next/head";
import Hero from "./components/Hero";
import About from "./components/About";
import Services from "./components/Services";
import Testimonials from "./components/Testimonials";
import Qualifications from "./components/Qualifications";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <>
      <Head>
        <title>Sacred Spirituality</title>
        <meta name="description" content="Unlock transformation. Book an appointment at Sacred Spirituality to unveil Reiki's healing power, seek energy work, and experience quality spiritual guidance." />
      </Head>
      <main>
        <Hero />
        <About />
        <Services />
        <Testimonials />
        <Qualifications />
        <Footer />
      </main>
    </>
  );
}
