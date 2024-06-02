import Header from "./Header";

const Hero = () => {
    return (
        <div>
            <section className="bg-cover bg-center h-screen font-sans text-center text-white">
                <Header />
                <div className="flex items-center justify-center min-h-screen bg-black bg-opacity-50">
                    <div className="flex flex-col items-center justify-center h-full m-4 sm:m-8 md:m-12 lg:m-16 xl:m-20 p-4 sm:p-8 md:p-12 lg:p-16 xl:p-20">
                        <h1 className="text-4xl md:text-6xl font-bold">Unveiling the Sacred Tapestry of Life</h1>
                        <p className="m-2 p-1 text-white">Discover the healing power of Reiki and embark on a journey of spiritual growth and self-discovery</p>
                        <button className="mt-4 px-6 py-2 bg-white text-black rounded-lg hover:bg-black hover:text-white transition duration-300">Book a Session</button>
                    </div>
                </div>
            </section>
        </div>
    )
};

export default Hero;
