import './App.css';
import { useState, useEffect } from "react";
import Something from './Something';

function App() {

  const [renderComponent, setRenderComponent] = useState(false)
  const [value, setValue] = useState(0)

  return (
    <div className="App">


      <button onClick={ ()=> {setRenderComponent(true)}}> Create </button>
      <button onClick={ ()=> {setRenderComponent(false)}}> Delete </button>
      <button onClick={ ()=> {setValue(Math.random() * 100)}}> Update </button>


      { renderComponent && <Something value={value}/>}
    </div>
  );
}

export default App;