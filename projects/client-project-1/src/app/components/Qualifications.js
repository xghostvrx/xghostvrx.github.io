import Image from 'next/image';

const Qualifications = () => (
    <section id="qualifications" className="p-8 bg-gray-100 text-center">
        <div className="mx-auto max-w-screen-lg">
            <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold
            bg-gradient-to-r from-green-400 via-yellow-500 to-pink-600 inline-block text-transparent bg-clip-text">Meet Your Spiritual Counselor</h2>
            <div className="my-4">
                <div className="rounded">
                    <Image src="/image-3.jpg" alt="Image of Doris Bennett" className="w-96 h-96 object-cover rounded-lg mx-auto shadow-lg" />
                </div>
                <h3 className="text-3xl md:text-4xl lg:text-5xl font-extrabold mt-4 text-yellow-500">Doris Bennett</h3>
                <p>Qualified Reiki Master & Spiritual Coach</p>
                <p className="mt-4 text-lg md:text-xl lg:text-2xl">
                    I know how it feels when the water stops running and you do not know where to turn. I have encountered many obstacles in my life. Being able to learn, adapt, and embrace my spirituality has allowed me to overcome and find purpose and fulfillment in my life.
                </p>
            </div>
            <hr className="my-4" />
            <div className="my-4">
                <h3 className="text-xl md:text-2xl lg:text-3xl font-bold">Certifications</h3>
                <ul className="mt-4 text-sm md:text-md lg:text-lg">
                    <li>Certified Chaplain (International&nbsp;Fellowship&nbsp;of&nbsp;Chaplains)</li>
                    <li>Advanced Reiki Training (Usui&nbsp;Shiki&nbsp;Ryoho&nbsp;Second&nbsp;Degree)</li>
                    <li>Certified Peer Support Specialist &&nbsp;Peer&nbsp;Recovery&nbsp;Mentor</li>
                </ul>
            </div>
            <hr className="my-4" />
            <p className="mt-4 text-lg md:text-xl lg:text-2xl">
                Through meditation, energy work, and ancient wisdom teachings, I assist you in cultivating a deep connection with your inner truth, allowing you to tap into the vast reservoir of wisdom and clarity that lies within. Whether you seek healing, personal growth, or a deeper sense of purpose, I will hold space for you to embrace your sacred essence and awaken to the boundless possibilities of your spiritual journey.
            </p>
        </div>
    </section>
);

export default Qualifications;
