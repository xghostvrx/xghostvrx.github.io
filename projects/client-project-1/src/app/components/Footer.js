'use client'
import { Link as ScrollLink, animateScroll as scroll } from 'react-scroll';

const Footer = () => (
    <footer className="flex flex-col md:flex-row justify-between items-center bg-white text-black text-center p-4 space-y-4 md:space-y-0">
        <div className="w-full md:w-auto text-center md:text-left">
            <ul className="space-y-2">
                <li className='underline hover:no-underline'>
                    <a href="https://squareup.com/appointments/book/25cxgqy11rmt2u/LGXFNZCX8XC4X/start">Appointments</a>
                </li>
            </ul>
        </div>
        <div className="flex flex-col md:flex-row items-center space-y-4 md:space-y-0 md:space-x-4">
            <div>
                <a href="" className="group">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" className="transition-colors duration-300 group-hover:text-red-500">
                        <path fill="currentColor" d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4zm9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8A1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5a5 5 0 0 1-5 5a5 5 0 0 1-5-5a5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3a3 3 0 0 0 3 3a3 3 0 0 0 3-3a3 3 0 0 0-3-3"></path>
                    </svg>
                </a>
            </div>
            <div className="text-center">
                <ScrollLink to="landing" smooth={true} duration={500} className='hover:text-yellow-500 transition duration-300 hover:cursor-pointer'>
                    <h2 className='text-2xl font-bold'>Sacred Spirituality</h2>
                </ScrollLink>
                <h3>Designed by Astroxios Software</h3>
            </div>
            <div>
                <a href="" className="group">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="currentColor" className="text-black group-hover:text-cyan-500 transition-colors duration-300">
                        <path d="M16.6 5.82s.51.5 0 0A4.278 4.278 0 0 1 15.54 3h-3.09v12.4a2.592 2.592 0 0 1-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6c0-1.72 1.66-3.01 3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64c0 3.33 2.76 5.7 5.69 5.7c3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 0 0 4.3 1.38V7.3s-1.88.09-3.24-1.48"></path>
                    </svg>
                </a>
            </div>
        </div>
        <div className="w-full md:w-auto text-center md:text-left">
            <ul className="space-y-2">
                <li>
                    <ScrollLink to="about" smooth={true} duration={500} className='underline hover:no-underline cursor-pointer'>
                        About
                    </ScrollLink>
                </li>
                <li>
                    <ScrollLink to="services" smooth={true} duration={500} className='underline hover:no-underline cursor-pointer'>
                        Services
                    </ScrollLink>
                </li>
                <li>
                    <ScrollLink to="testimonials" smooth={true} duration={500} className='underline hover:no-underline cursor-pointer'>
                        Testimonials
                    </ScrollLink>
                </li>
            </ul>
        </div>
    </footer>
);

export default Footer;
