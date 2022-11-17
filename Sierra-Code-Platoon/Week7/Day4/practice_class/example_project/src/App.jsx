import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'


function Subtract({number, setSubtract}){
  function onClick(){
    setSubtract((number) => number - 1)}
  
  return(
    <button onClick={onClick}>
      difference is {number}
    </button>
  )
}

function MultiplyBy2({number, setSubtract}){
  function onClick(){
    setSubtract((number) => number * 2)}
  
  return(
    <button onClick={onClick}>
      Product is {number}
    </button>
  )
}

function App() {
  const [number, setSubtract] = useState(100)

  return (
    <div className="App">
      
      <h1> Subtract </h1>
      <Subtract number={number} setSubtract = {setSubtract}/>
      <p> Mutate</p>
      <MultiplyBy2 number={number} setSubtract = {setSubtract}/>
      
    </div>
  )
}

export default App
