import { useState } from 'react';
import Count2 from './components/Count2';
import CountNumerList from './components/CountNumerList';
import InputUseAlert from './components/InputUseAlert';
import InputWith2Fields from './components/InputWith2Fileds';
import OnAndOff from './components/OnAndOff';
import InputPrint from './components/InputPrint';
import ReadAndView from './components/ReadAndView';


// import './App.css'

function App() {

  const lst = [5,6,7,8,9,10];

  return (
    <div className="App">
      <CountNumerList/>
      <Count2 numbers={lst}/>
      <div> <OnAndOff/> </div>
      <InputUseAlert/>
      <InputWith2Fields/>
      <InputPrint/>
      <ReadAndView/>
    </div>
  )
}

export default App
