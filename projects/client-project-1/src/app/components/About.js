const About = () => (
    <section className="p-4 md:p-8 bg-white text-center">
        <div>
            <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold">Your Reiki Master</h2>
            <p className="mt-4 text-lg md:text-xl lg:text-2xl">
                I am a spiritual counselor who provides quality life and motivational guidance. My passion for sacred spirituality is rooted in a deep reverence for the interconnectedness of all beings and the profound wisdom that resides within each of us. Through the ancient practice of Reiki, I act as a conduit for the universal life force energy, facilitating the natural healing process and restoring balance and harmony within the mind, body, and spirit.
            </p>
            <button className="mt-4 px-6 py-2 text-base md:text-lg lg:text-xl bg-gray-200 text-black rounded hover:bg-black hover:text-white transition duration-300">
                Learn More
            </button>
        </div>
        <div className="flex flex-col md:flex-row my-8 p-1">
            <img src="https://placehold.co/250x250" alt="Image of a reiki space with candles" className="w-full md:w-1/2 lg:w-1/3 h-64 object-cover rounded mb-4 md:mb-0 md:mr-8 mx-auto" />
            <div className="text-center md:text-left">
                <h3 className="text-2xl md:text-3xl lg:text-4xl">Providing you a safe space to release</h3>
                <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">
                    Your appointment will take place in a safe, private setting, all of which accompanies personalized care.
                </p>
            </div>
        </div>
        <div className="flex flex-col md:flex-row-reverse my-8 p-1">
            <img src="https://placehold.co/250x250" alt="Image of a reiki space with candles" className="w-full md:w-1/2 lg:w-1/3 h-64 object-cover rounded mb-4 md:mb-0 md:ml-8 mx-auto" />
            <div className="text-center md:text-left">
                <h3 className="text-2xl md:text-3xl lg:text-4xl">In-person and remote options</h3>
                <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">
                    You can choose to experience the transformative power of our sessions in the sanctuary of my office space, allowing you to fully immerse yourself in the sacred energy. Or, if you prefer the comfort and privacy of your own space, I am delighted to visit you at home, a location of your choosing, or online.
                </p>
            </div>
        </div>
    </section>
);

export default About;
