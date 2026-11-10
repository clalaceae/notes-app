import styles from './css/Sidebar.module.css'
import Suzume from '../assets/Suzume.jpg'
import { 
  PanelLeftOpen,
  PanelLeftClose,
  FilterX,
  Filter,
  CalendarDays,
  RefreshCcw,
  RefreshCcwDot,
  Settings
} from 'lucide-react'

export function Sidebar() {

  return (
    <aside className={styles.sb}>
      <img aria-label='App Icon' src={Suzume}/>
      <button aria-label='Expand'>
        {/* expand or minimise, and icon */}
        { true ? <PanelLeftOpen/> : <PanelLeftClose/> }
        </button>
      <button aria-label='Filter'>
        {/* none or has */}
        { true ? <FilterX/> : <Filter/> }
        </button>
      <button aria-label='Calendar'>
        <CalendarDays/>
        </button>
      <button aria-label='Sync'>
        {/* label to Ready or Done, and icon*/}
        { true ? <RefreshCcw/> : <RefreshCcwDot/> }
        </button>
      <button aria-label='Settings'>
        <Settings/>
        </button>
    </aside>
  )
}

export default Sidebar