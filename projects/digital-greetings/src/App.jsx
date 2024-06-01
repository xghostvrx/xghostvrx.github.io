import React, { useState } from 'react';
import Confetti from 'react-confetti';
import landing from './assets/landing.gif';
import surprise from './assets/surprise.gif';

function App() {
  const [showSurprise, setShowSurprise] = useState(false);
  const [name] = useState('Meri the cutie');
  const [message] = useState('Surprise, baby! Today is going to be a fantastic day! I love you so much!');

  const handleButtonClick = () => {
    setShowSurprise(true);
  };

  if (showSurprise) {
    document.title = `Happy Birthday, ${name}!`;
  } else {
    document.title = "Guess what?!";
  }

  return (
    <>
      <div className='flex justify-center items-center h-screen'>
        <div className='text-center'>
          {!showSurprise && <h1 className='text-5xl'>Guess what?!</h1>}
          {showSurprise && <Confetti />}
          {showSurprise && <h1 className='text-5xl font-bold mb-4'>Happy Birthday, {name}!</h1>}
          {showSurprise && <h2 className='text-xl mb-4'>{message}</h2>}
          <img
            src={showSurprise ? surprise : landing}
            alt={showSurprise ? 'Surprise' : 'Tejiendo Gatito'}
            className='mx-auto mb-8'
          />
          {!showSurprise && (
            <button
              onClick={handleButtonClick}
              className='bg-slate-100 hover:bg-pink-500 hover:text-white py-4 px-8 text-2xl rounded-lg button-effect'
            >
              Press for a Surprise
            </button>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
