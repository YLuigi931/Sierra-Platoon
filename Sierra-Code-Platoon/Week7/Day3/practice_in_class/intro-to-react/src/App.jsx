import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

import ButtonCounter from "./components/ButtonCounter";

function App() {
  
  return (
    <div className="App">
      <ButtonCounter/>
      <ButtonCounter/>
      <ButtonCounter/>
    </div>
  )
}

export default App;