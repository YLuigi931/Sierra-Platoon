import './App.css';
import { Component } from "react"
import { useState, useEffect } from 'react'

// components
import ErrorDisplay from './components/ErrorDisplay';
import InputZipCode from './components/InputZipCode';
import TemperatureDisplay from './components/TemperatureDisplay';

// API KEY
const myOpenWeatherApiKey = "83491f3157b47f6402bd6a96ecb391c3" /* <-- replace with your api key here (using https://home.openweathermap.org/api_keys)*/

function App() {
  // states
  const[temperature, setTemperature] = useState(null);
  const[zipCode, setZipCode] = useState("");

  // state = {
  //   temperature: null,
  //   zipCode: ""
  // }

  // effects
  const getTemperature = async ()=> {
    try {
      console.log("obtaining temperature...")
      let response = await fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${this.state.zipCode},us&appid=${myOpenWeatherApiKey}`)
      
      if (response.ok) {
        let data = await response.json()
        if (data) {
          setTemperature(data.main.temp)
        }
      }
      else {
        setTemperature(null)
      }
    }
    catch (e) {
      console.error(e)
    }
  }

  // componentDidUpdate(prevProps, prevState) {
  //   if (prevState.zipCode !== this.state.zipCode) {
  //     this.getTemperature()
  //   }
  // }

  useEffect( () => {
    getTemperature()
  }, [zipCode]);

  // handlers
  let updateZipCode = (newZipCode) => {
    this.setState({zipCode: newZipCode})
  }

  // render
  function renderDisplay(){
    // don't show any display if no zip code has been entered
    if (!zipCode) {
      return null
    }
    // show an error if we don't get back valid data
    else if (!temperature) {
      return <ErrorDisplay message="Unable to get temperature information from your zip code." />
    }
    
    return (
      <div className="App">
        <h1> Temperature Output </h1>
        <TemperatureDisplay tempInKelvin={temperature}/>
      </div>
    )
  }
  
  return (
    <div className="App">
      <h2>Temperature Conversion App</h2>
      <InputZipCode updateZipCode={updateZipCode} buttonText="Get Temperature"/>
      { renderDisplay() }
    </div>
  );
  
}

export default App;
