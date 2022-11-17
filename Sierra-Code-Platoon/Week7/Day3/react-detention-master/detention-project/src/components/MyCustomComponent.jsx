import { useState } from "react"

function MyCustomComponent() {

    // states
    const [counter, setCounter] = useState(0)
    // event handlers
    const increamentCounter = () =>{
        setCounter(counter + 1)
    }
    // render

    return (
        <div>
            <button id="my-button" onClick={increamentCounter}> Click Me! </button>
            <p id="my-output"> YOu've clicked the button {counter} times. </p>
        </div>
    )
    
}

export default MyCustomComponent;