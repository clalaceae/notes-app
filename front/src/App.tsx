import './App.css'
import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import { usePreventPinchZoom } from './hooks/usePreventPinchZoom'

function App() {
  usePreventPinchZoom()

  return (
    <Routes>
      <Route path="/" element={<Home />}/>
    </Routes>
  )
}

export default App
