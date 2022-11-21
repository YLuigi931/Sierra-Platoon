import { useState } from 'react'

function Reverse(){
    const[word, setWord]= useState('')
    const handleChange = (e) =>{
        setWord(e.target.value)
    }

    

    return (
        <div>
            <input placeholder="Enter word" onChange={word}/>
            <button onClick={onClick}> Check if Palindrome </button>
            <p>{word}</p>
        </div>
    )
}


export default Reverse