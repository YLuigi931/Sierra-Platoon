import {useState} from 'react'

export default function GetVowels(){
    const[counter, setCounter] = useState(0);
    const[subject, setSubject] = useState('');
    const clickHandler = (e) => {
    // const flip = subject.toLowerCase.split("").reverse().join("");
        const vowels = ['a','e','i','o','u'] 
        alert(`This was submit ${subject.toLowerCase()}`)
        let count = 0 ;
        let temp = subject.toLowerCase()
        
        temp.split("").forEach(char => { 
            
        }) 
        setCounter(count);
        
    }

    return (
        <div>
            <form onSubmit={clickHandler}>
                <label> Enter the word here:
                    <input type="text" value={subject} onChange={(e)=>{
                        setSubject(e.target.value)
                    }}/>
                    
                </label>
                <input type="submit"/>
            </form>
        </div>
    )
}