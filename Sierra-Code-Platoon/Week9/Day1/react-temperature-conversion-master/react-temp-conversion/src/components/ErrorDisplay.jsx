import { Component } from "react"

import { useEffect } from 'react';

export default function ErrorDisplay({props}) {


  useEffect(() => {
    console.log("!! There was an error !!");
  }, []);

  useEffect(() => {
    console.log("++ The error was resolved ++");
  }, []);
  
  return (
      <div>
        <p className="error">Error: { props.message }</p>
      </div>
    ) 
}