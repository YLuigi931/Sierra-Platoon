import { useState } from 'react'

export default function InputUseAlert(){

    const[text,setText] = useState("");

    const handle_Button = (event) => {
        event.preventDefault();
        alert(`The name you entered was: ${text}`);
    }

    return(
        <form onSubmit={handle_Button}>
            <label>Enter your Name:
                <input 
                    text="text" 
                    value={text} 
                    onChange={(e) => setText(e.target.value)}
                    />
                    <input type="submit"/>
            </label>
        </form>
    )
}