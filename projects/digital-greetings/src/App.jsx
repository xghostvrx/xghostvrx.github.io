import landing from './assets/tejiendo-gatito.gif'
import surprise from './assets/surprise.gif'

function App() {

  return (
    <>
      <div className='flex justify-center items-center h-screen'>
        <div className='text-center'>
          <img src={landing} alt="Tejiendo Gatito" className='mx-auto mb-4'></img>
          <img src={surprise} alt="Surprise" className='mx-auto mb-4'></img>
          <button className='bg-slate-100 hover:bg-pink-500 hover:text-white py-2 px-4 rounded-lg button-effect'>Press for a Surprise</button>
        </div>
      </div>
    </>
  )
}

export default App
