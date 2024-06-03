import Header from "./Header";

const Hero = () => {
    return (
        <section className="parallax h-screen font-sans text-center text-white">
            <Header />
            <div className="flex items-center justify-center min-h-screen bg-slate-600 bg-opacity-30">
                <div className="flex flex-col items-center justify-center h-full m-4 p-4">
                    <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold">
                        Discover the Sacred Path to Spiritual&nbsp;Awareness
                    </h1>
                    <p className="mt-2 md:mt-4 p-1 text-white text-lg md:text-xl lg:text-2xl">
                        Discover the healing power of Reiki and embark on a journey of&nbsp;spiritual&nbsp;growth&nbsp;and&nbsp;self-discovery.
                    </p>
                    <a href="https://squareup.com/appointments/book/25cxgqy11rmt2u/LGXFNZCX8XC4X/start">
                        <button className="mt-4 px-6 py-2 text-base md:text-lg lg:text-xl bg-white text-black rounded hover:bg-black hover:text-white transition duration-300">
                            Book a Session
                        </button>
                    </a>
                </div>
            </div>
        </section>
    );
};

export default Hero;
