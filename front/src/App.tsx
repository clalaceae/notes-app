import { useState } from 'react'
import './App.css'
import { fetchHelper } from './api'

type CheckRes = {
  status: string
}


function App() {
  const [status, setStatus] = useState('')
  
  const checkDB = async () => {
    setStatus('Checking backend...')

    try {
      const data = await fetchHelper<CheckRes>('/api/test')
      setStatus(data.status)
    } catch (error) {
      console.error(error)
      setStatus('Could not reach backend')
    }
  }

  return (
    <>
      <button onClick={checkDB}>Check backend</button>
      <p>Backend: {status}</p>
    </>
  )
}

export default App
