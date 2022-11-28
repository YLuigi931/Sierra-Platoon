import { Component,useEffect, useRef } from "react"


function Something(props) {
  
  // effects
  useEffect(() => { // the ordering of the useEffect matters here, because firstRender.current is set to false in the second useEffect
    if (!firstRender.current) {
      // componentDidUpdate()
      console.log("componentDidUpdate: I AM UPDATING NOW!")
    }
  }, [props.value])
  
  useEffect(() => {
    // componentDidMount
    console.log("componentDidMount: I AM ALIVE NOW!")
    firstRender.current = false
    
    // componentWillUnmount
    return () => console.log("componentWillUnmount: I AM DYING NOW!")
  }, [])

  // render
  
    return (
      <div>
        The value is { props.value }
      </div>
    )
  
}

export default Something;