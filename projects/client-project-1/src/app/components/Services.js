const Services = () => (
    <section id="services" className="p-4 md:p-8 bg-gray-100 text-center">
        <div className="flex flex-col items-center mx-auto max-w-screen-lg">
            <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-8">Services</h2>

            <div className="flex flex-wrap justify-center w-full">
                <div className="m-4 p-4 flex flex-col items-center">
                    <img src="https://placehold.co/100x100" className="w-full max-w-xs h-64 object-cover rounded mb-4 border-8 border-black" alt="Service 1" />
                    <div className="text-center">
                        <h3 className="text-2xl md:text-3xl lg:text-4xl">Reiki Healing Sessions</h3>
                        <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Discover the healing power&nbsp;of&nbsp;Reiki</p>
                    </div>
                </div>
                <div className="m-4 p-4 flex flex-col items-center">
                    <img src="https://placehold.co/100x100" className="w-full max-w-xs h-64 object-cover rounded mb-4 border-8 border-black" alt="Service 2" />
                    <div className="text-center">
                        <h3 className="text-2xl md:text-3xl lg:text-4xl">Spiritual Counseling</h3>
                        <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Embark on a journey of&nbsp;spiritual&nbsp;growth</p>
                    </div>
                </div>
                <div className="m-4 p-4 flex flex-col items-center">
                    <img src="https://placehold.co/100x100" className="w-full max-w-xs h-64 object-cover rounded mb-4 border-8 border-black" alt="Service 3" />
                    <div className="text-center">
                        <h3 className="text-2xl md:text-3xl lg:text-4xl">1-on-1 Guided Meditations</h3>
                        <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Experience the transformative&nbsp;power</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
);

export default Services;
