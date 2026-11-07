import { type ReactNode } from 'react'
import {Sidebar} from './Sidebar'
import styles from './css/Layout.module.css'

type LayoutProps = {
  children?: ReactNode
}

export function Layout({ children }: LayoutProps) {
  return (
    <div className={styles.layout}>
      <Sidebar />
      <main>{children}</main>
    </div>
  )
}

export default Layout
