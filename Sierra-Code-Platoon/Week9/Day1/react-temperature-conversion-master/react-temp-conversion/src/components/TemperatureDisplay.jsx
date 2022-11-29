import { Component } from "react"
import { useState, useEffect } from 'react'

export default function TemperatureDisplay(props) {
  // NOTE: Yes, you probably can refactor this component to eliminate these state values, but we've added them for the sake of understanding life-cycle methods better, so please do not remove them. 

  // state
  // state = {
  //   tempInCelsius: null,
  //   tempInFahrenheit: null
  // }

  const[tempInCelsius, setTempInCelsius] = useState(null);
  const[tempInFahrenheit, setTempInFahrenheit] = useState(null);

  // effects
  function updateTempValues() {
    let tC = props.tempInKelvin - 273.15;
    let tF = (tC * 9 / 5) + 32;

    // this.setState({
    //   tempInCelsius: tC.toFixed(2),
    //   tempInFahrenheit: tF.toFixed(2)
    // })
    setTempInCelsius(tC.toFixed(2));
    setTempInFahrenheit(tF.toFixed(2));

  }

  // componentDidMount() {
  //   this.updateTempValues()
  // }

  useEffect(() => {
    updateTempValues();
  },[props.tempInKelvin]);

  // componentDidUpdate(prevProps, prevState) {
  //   if (prevProps.tempInKelvin !== this.props.tempInKelvin) {
  //     this.updateTempValues()
  //   }
  // }

    return (
      <div>
        <p>Current Temperature:</p>
        <span className="temperature">
          { tempInCelsius }
          <span className="units">°C</span>
          &nbsp;&nbsp;&nbsp;&nbsp; 
          { tempInFahrenheit }
          <span className="units">°F</span>
        </span>
      </div>
    )
}