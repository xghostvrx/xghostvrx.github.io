// components/Footer.js
import Link from 'next/link';

const Footer = () => (
    <footer className="flex justify-between items-center bg-white text-black text-center p-4">
        <div>
            <ul>
                <li><Link href="/appointments" className='underline hover:no-underline'>Appointments</Link></li>
            </ul>
        </div>
        <div className='flex'>
            <div>
                <a href="">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24"><path fill="#000000" d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4zm9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8A1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5a5 5 0 0 1-5 5a5 5 0 0 1-5-5a5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3a3 3 0 0 0 3 3a3 3 0 0 0 3-3a3 3 0 0 0-3-3"></path></svg>
                </a>
            </div>
            <div className='mx-2'>
                <h2 className='text-2xl font-bold'>Sacred Spirituality</h2>
                <h3>Designed by Astroxios Software</h3>
            </div>
            <div>
                <a href="">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24"><path fill="#000000" d="M16.6 5.82s.51.5 0 0A4.278 4.278 0 0 1 15.54 3h-3.09v12.4a2.592 2.592 0 0 1-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6c0-1.72 1.66-3.01 3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64c0 3.33 2.76 5.7 5.69 5.7c3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 0 0 4.3 1.38V7.3s-1.88.09-3.24-1.48"></path></svg>
                </a>
            </div>
        </div>
        <div>
            <ul className='text-left'>
                <li><Link href="#about" className='underline hover:no-underline'>About</Link></li>
                <li><Link href="#services" className='underline hover:no-underline'>Services</Link></li>
                <li><Link href="#testimonials" className='underline hover:no-underline'>Testimonials</Link></li>
            </ul>
        </div>
    </footer>
);

export default Footer;
