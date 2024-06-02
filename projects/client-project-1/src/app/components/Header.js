import Link from 'next/link';

const Header = () => (
    <header className="absolute w-full bg-transparent font-sans text-lg md:text-2xl text-white p-4 md:p-8">
        <nav className="flex justify-between">
            <Link href="/" className='hover:text-black transition duration-300'>Sacred Spirituality</Link>
            <div className="flex space-x-10">
                <Link href="#about" className='hover:text-black transition duration-300'>About</Link>
                <Link href="#services" className='hover:text-black transition duration-300'>Services</Link>
                <Link href="#testimonials" className='hover:text-black transition duration-300'>Testimonials</Link>
            </div>
        </nav>
    </header>
);

export default Header;
