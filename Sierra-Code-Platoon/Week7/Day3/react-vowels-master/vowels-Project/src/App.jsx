import { useState } from 'react'

import './App.css'
import GetVowels from './components/GetVowels'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <GetVowels/>
    </div>
  )
}

export default App
