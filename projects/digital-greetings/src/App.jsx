import React, { useState } from 'react';
import Confetti from 'react-confetti';
import landing from './assets/tejiendo-gatito.gif';
import surprise from './assets/surprise.gif';

function App() {
  const [showSurprise, setShowSurprise] = useState(false);

  const handleButtonClick = () => {
    setShowSurprise(true);
  };

  return (
    <>
      <div className='flex justify-center items-center h-screen'>
        <div className='text-center'>
          <h1 className='text-5xl'>Guess what?!</h1>
          {showSurprise && <Confetti />}
          {showSurprise && <h1 className='text-5xl font-bold mb-4'>Happy Birthday</h1>}
          <img
            src={showSurprise ? surprise : landing}
            alt={showSurprise ? 'Surprise' : 'Tejiendo Gatito'}
            className='mx-auto mb-8'
          />
          {!showSurprise && (
            <button
              onClick={handleButtonClick}
              className='bg-slate-100 hover:bg-pink-500 hover:text-white py-2 px-4 rounded-lg button-effect'
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
