import Header from "./Header";

const Hero = () => {
    return (
        <div>
            <section className="bg-cover bg-center h-screen font-sans text-center text-white relative" style={{ backgroundImage: "url('/background.jpg')" }}>
                <div className="film-grain absolute inset-0 z-10"></div>
                <Header />
                <div className="flex items-center justify-center min-h-screen bg-black bg-opacity-30 relative z-10">
                    <div className="flex flex-col items-center justify-center h-full m-4 p-4">
                        <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold">
                            Discover the Sacred Path to&nbsp;Spiritual&nbsp;Enlightenment
                        </h1>
                        <p className="mt-2 md:mt-4 p-1 text-white text-lg md:text-xl lg:text-2xl">
                            Discover the healing power of Reiki and embark on a journey of spiritual&nbsp;growth&nbsp;and&nbsp;self-discovery.
                        </p>
                        <button className="mt-4 px-6 py-2 text-base md:text-lg lg:text-xl bg-white text-black rounded hover:bg-black hover:text-white transition duration-300">
                            Book a Session
                        </button>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Hero;
