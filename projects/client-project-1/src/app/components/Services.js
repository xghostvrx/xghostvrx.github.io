
const Services = () => (
    <section id="services" className="p-4 md:p-8 bg-gray-100 text-center">
        <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold">Services</h2>
        <div className="mt-4 flex flex-col md:flex-row justify-around items-center">
            <div className="m-4">
                <img src="https://placehold.co/100x100" className="w-full h-64 object-cover rounded mb-4 mx-auto"></img>
                <h3 className="text-2xl md:text-3xl lg:text-4xl">Reiki Healing Sessions</h3>
                <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Discover the healing power of Reiki...</p>
            </div>
            <div className="m-4">
                <img src="https://placehold.co/100x100" className="w-full h-64 object-cover rounded mb-4 mx-auto"></img>
                <h3 className="text-2xl md:text-3xl lg:text-4xl">Spiritual Counseling</h3>
                <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Embark on a journey of spiritual growth...</p>
            </div>
            <div className="m-4">
                <img src="https://placehold.co/100x100" className="w-full h-64 object-cover rounded mb-4 mx-auto"></img>
                <h3 className="text-2xl md:text-3xl lg:text-4xl">1-on-1 Guided Meditations</h3>
                <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">Experience the transformative power...</p>
            </div>
        </div>
    </section>
);

export default Services;
