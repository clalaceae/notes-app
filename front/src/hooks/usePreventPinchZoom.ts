import { useEffect } from 'react'

export function usePreventPinchZoom() {
  useEffect(() => {
    function handleWheel(event: WheelEvent) {
      if (event.ctrlKey && event.cancelable) {
        event.preventDefault()
      }
    }

    document.addEventListener('wheel', handleWheel, { passive: false })

    return () => {
      document.removeEventListener('wheel', handleWheel)
    }
  }, [])
}