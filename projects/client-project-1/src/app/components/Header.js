'use client'
import { useState, useEffect } from 'react';
import Link from 'next/link';
import { Link as ScrollLink } from 'react-scroll';
import classNames from 'classnames';

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    }

    useEffect(() => {
        if (menuOpen) {
            document.body.classList.add('overflow-hidden');
        } else {
            document.body.classList.remove('overflow-hidden');
        }

        return () => {
            document.body.classList.remove('overflow-hidden');
        };
    }, [menuOpen]);

    return (
        <header className="absolute w-full bg-transparent font-sans text-2xl text-white p-4 md:p-8">
            <nav className="flex justify-between">
                <Link href="/" className='hover:text-black transition duration-300'>Sacred Spirituality</Link>
                <div className="hidden md:flex space-x-10">
                    <ScrollLink
                        to="about"
                        smooth={true}
                        duration={500}
                        className='hover:text-black transition duration-300 cursor-pointer'
                    >
                        About
                    </ScrollLink>

                    <ScrollLink
                        to="services"
                        smooth={true}
                        duration={500}
                        className='hover:text-black transition duration-300 cursor-pointer'
                    >
                        Services
                    </ScrollLink>

                    <ScrollLink
                        to="testimonials"
                        smooth={true}
                        duration={500}
                        className='hover:text-black transition duration-300 cursor-pointer'
                    >
                        Testimonials
                    </ScrollLink>
                </div>
                <div className="md:hidden z-10">
                    <button onClick={toggleMenu}>
                        <div className={classNames(`tham tham-e-squeeze tham-w-6`, { 'tham-active': menuOpen })}>
                            <div className="tham-box">
                                <div className={classNames("tham-inner", { "bg-black": menuOpen, "bg-white": !menuOpen })} />
                            </div>
                        </div>
                    </button>
                </div>
            </nav>
            {menuOpen && (
                <div className="fixed inset-0 bg-white bg-opacity-95 flex flex-col items-center justify-center space-y-6 transition-opacity duration-300 text-4xl">
                    <ScrollLink
                        to="about"
                        smooth={true}
                        duration={500}
                        onClick={() => setMenuOpen(false)}
                        className="block text-black hover:text-slate-600 transition duration-300 cursor-pointer"
                    >
                        About
                    </ScrollLink>

                    <ScrollLink
                        to="services"
                        smooth={true}
                        duration={500}
                        onClick={() => setMenuOpen(false)}
                        className="block text-black hover:text-slate-600 transition duration-300 cursor-pointer"
                    >
                        Services
                    </ScrollLink>

                    <ScrollLink
                        to="testimonials"
                        smooth={true}
                        duration={500}
                        onClick={() => setMenuOpen(false)}
                        className="block text-black hover:text-slate-600 transition duration-300 cursor-pointer"
                    >
                        Testimonials
                    </ScrollLink>
                </div>
            )}
        </header>
    );
};

export default Header;
