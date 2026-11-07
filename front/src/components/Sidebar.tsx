import styles from './css/Sidebar.module.css'
import Suzume from '../assets/Suzume.jpg'
import { PanelLeftOpen, Settings } from 'lucide-react'

export function Sidebar() {

  return (
    <aside className={styles.sb}>
      <img aria-label='App Icon' src={Suzume}>
        </img>
      <button aria-label='Menu'>
        <PanelLeftOpen/>
        </button>
      <button aria-label='Settings'>
        <Settings/>
        </button>
    </aside>
  )
}

export default Sidebar
