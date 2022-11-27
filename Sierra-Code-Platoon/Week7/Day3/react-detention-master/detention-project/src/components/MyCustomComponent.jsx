import { useState } from "react"


function MyCustomComponent() {
    
    // states
    const[messages, setMessages] = useState([]);
    
    function display100Messages(){

        let newMessages = []
       
        for(let i=1; i<=100; i++){
    
          newMessages.push(<li key={`${i}`}>{`this is message ${i}`}</li>)
        }
        
        return newMessages
    }

    // render
    return (
        <div>
            <ul>
                {display100Messages()}  
            </ul>
        </div>
    )
    
}

export default MyCustomComponent;