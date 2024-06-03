'use client'
import { useState } from 'react';
import Link from 'next/link';

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    }

    return (
        <header className="absolute w-full bg-transparent font-sans text-lg md:text-2xl text-white p-4 md:p-8">
            <nav className="flex justify-between">
                <Link href="/" className='hover:text-black transition duration-300'>Sacred Spirituality</Link>
                <div className="hidden md:flex space-x-10">
                    <Link href="#about" className='hover:text-black transition duration-300'>About</Link>
                    <Link href="#services" className='hover:text-black transition duration-300'>Services</Link>
                    <Link href="#testimonials" className='hover:text-black transition duration-300'>Testimonials</Link>
                </div>
                <div className="md:hidden">
                    <button onClick={toggleMenu} className='focus:outline-none'>
                        <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={menuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"}></path>
                        </svg>
                    </button>
                </div>
            </nav>
            {menuOpen && (
                <div className='md:hidden mt-4 space-y-4'>
                    <Link href="#about" className="block hover:text-black transition duration-300">About</Link>
                    <Link href="#services" className="block hover:text-black transition duration-300">Services</Link>
                    <Link href="#testimonials" className="block hover:text-black transition duration-300">Testimonials</Link>
                </div>
            )}
        </header>
    );
};

export default Header;
