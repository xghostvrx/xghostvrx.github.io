import Header from "./Header";

const Hero = () => {
    return (
        <div>
            <section className="bg-cover bg-center h-screen font-sans text-center text-white relative" style={{ backgroundImage: "url('/background.jpg')" }}>
                <div className="film-grain absolute inset-0 z-10"></div>
                <Header />
                <div className="flex items-center justify-center min-h-screen bg-black bg-opacity-30 relative z-10">
                    <div className="flex flex-col items-center justify-center h-full m-4 p-4">
                        <h1 className="text-4xl md:text-6xl font-bold">
                            Discover the Sacred Path to Spiritual&nbsp;Enlightenment
                        </h1>
                        <p className="m-2 p-1 text-white">Discover the healing power of Reiki and embark on a journey of spiritual&nbsp;growth&nbsp;and&nbsp;self-discovery.</p>
                        <button className="mt-4 px-6 py-2 bg-white text-black rounded-lg hover:bg-black hover:text-white transition duration-300">Book a Session</button>
                    </div>
                </div>
            </section>
        </div>
    )
};

export default Hero;
