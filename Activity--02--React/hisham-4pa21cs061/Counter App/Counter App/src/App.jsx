import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <button onClick={()=>setCount(count=>count+1)}>You clicked me: {count} times!</button>
    </>
  )
}

export default App
