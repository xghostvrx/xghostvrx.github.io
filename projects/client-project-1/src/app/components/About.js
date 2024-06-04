'use client'
import React, { useState } from 'react';
import Image from 'next/image';

const About = () => {
    const [showModal, setShowModal] = useState(false);

    return (
        <section id="about" className="p-4 md:p-8 bg-white text-center">
            <div className="mx-auto max-w-screen-lg">
                <div>
                    <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold
                    bg-gradient-to-r from-purple-600 via-orange-500 to-blue-400 inline-block text-transparent bg-clip-text">What is Sacred Spirituality?</h2>
                    <p className="mt-4 text-lg md:text-xl lg:text-2xl">
                        I am a spiritual counselor who provides quality life and motivational guidance. My passion for sacred spirituality is rooted in a deep reverence for the interconnectedness of all beings and the profound wisdom that resides within each of us. Through the ancient practice of Reiki, I act as a conduit for the universal life force energy, facilitating the natural healing process and restoring balance and harmony within the&nbsp;mind,&nbsp;body,&nbsp;and&nbsp;spirit.
                    </p>

                    <button
                        className="mt-4 px-6 py-2 text-base md:text-lg lg:text-xl bg-gray-200 text-black rounded hover:bg-black hover:text-white transition duration-300"
                        onClick={() => setShowModal(true)}
                    >
                        Learn More
                    </button>
                    {showModal && (
                        <div className="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
                            <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                                <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
                                <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                                <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full">
                                    <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                                        <h2 className="text-2xl font-bold mb-4 text-yellow-500">Tapping Into Reiki&apos;s Healing Energy</h2>
                                        <p className="text-gray-700 mb-4">
                                            In our fast-paced, always-on world, it&apos;s easy to lose touch with ourselves and the natural flow of energy within and around us. Stress, negativity, and energy blockages can profoundly impact our mind, body and spirit in ways we may not even realize. Understanding the importance of restoring balance and allowing positive energy to flow freely is therefore important for our health.
                                        </p>
                                        <p className="text-gray-700 mb-4">
                                            Reiki is an ancient Japanese healing modality that can help restore energetic harmony and promote profound levels of relaxation, reducing stress and pain while activating the body&apos;s innate ability to heal itself.
                                        </p>
                                        <p className="text-gray-700 mb-4">
                                            The term Reiki translates to &quot;universal life force energy,&quot; and the practice is based on the belief that we are all living, breathing sources of this vital force that animates all living beings. When our life force energy becomes blocked, stagnant or disrupted, we are more likely to experience a wide range of physical, mental and emotional issues. Reiki helps break up these energetic blockages and facilitates the free flow of energy once again.
                                        </p>
                                        <p className="text-gray-700 mb-4">
                                        &quot;So many of the symptoms and conditions we experience, like pain, fatigue, anxiety and tension, are a result of our life force being out of balance and unable to circulate properly,&quot; explains Reiki Master Doris Bennett. &quot;Through a Reiki session, we are able to dissolve the blockages and support the body&apos;s natural ability to heal and regulate itself.&quot;
                                        </p>
                                        <p className="text-purple-700 font-bold mb-4">
                                            If you have been feeling stuck or simply depleted, booking a Reiki session, meditation or spiritual consultation could be what you have been needing.
                                        </p>
                                    </div>
                                    <div className="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                                        <button type="button" className="mt-3 w-full inline-flex justify-center rounded border border-transparent shadow-sm px-4 py-2 bg-gray-200 text-base font-medium text-black hover:bg-black hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-black sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm transition-colors duration-200" onClick={() => setShowModal(false)}>
                                            Close
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                </div>
                <div className="flex flex-col md:flex-row my-8 p-1">
                    <Image src="/image-1.jpg" alt="Image of a reiki space with candles" className="w-full h-96 object-cover rounded mb-4 md:mb-0 md:mr-8 mx-auto  shadow-lg" />
                    <div className="text-center md:text-left">
                        <h3 className="text-2xl md:text-3xl lg:text-4xl">Providing you a safe space to release</h3>
                        <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">
                            Your appointment will take place in a safe, private setting, all of which accompanies personalized care.
                        </p>
                    </div>
                </div>
                <div className="flex flex-col md:flex-row-reverse my-8 p-1">
                    <Image src="/image-2.jpg" alt="Image of a reiki space with candles" className="w-full h-80 object-cover rounded mb-4 md:mb-0 md:ml-8 mx-auto shadow-lg" />
                    <div className="text-center md:text-left">
                        <h3 className="text-2xl md:text-3xl lg:text-4xl">In-person and remote options</h3>
                        <p className="mt-2 md:mt-4 text-lg md:text-xl lg:text-2xl">
                            You can choose to experience the transformative power of our sessions in the sanctuary of my office space, allowing you to fully immerse yourself in the sacred energy. Or, if you prefer the comfort and privacy of your own space, I am delighted to visit you at home, a location of your choosing, or online.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default About;
