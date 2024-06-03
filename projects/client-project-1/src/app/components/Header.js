'use client'
import { useState } from 'react';
import Link from 'next/link';
import classNames from 'classnames';

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    }

    return (
        <header className="absolute w-full bg-transparent font-sans text-2xl text-white p-4 md:p-8">
            <nav className="flex justify-between">
                <Link href="/" className='hover:text-black transition duration-300'>Sacred Spirituality</Link>
                <div className="hidden md:flex space-x-10">
                    <Link href="#about" className='hover:text-black transition duration-300'>About</Link>
                    <Link href="#services" className='hover:text-black transition duration-300'>Services</Link>
                    <Link href="#testimonials" className='hover:text-black transition duration-300'>Testimonials</Link>
                </div>
                <div className="md:hidden">
                    <button onClick={toggleMenu}>
                        <div className={classNames(`tham tham-e-squeeze tham-w-6`, { 'tham-active': menuOpen })}>
                            <div className="tham-box">
                                <div className="tham-inner bg-white" />
                            </div>
                        </div>
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
