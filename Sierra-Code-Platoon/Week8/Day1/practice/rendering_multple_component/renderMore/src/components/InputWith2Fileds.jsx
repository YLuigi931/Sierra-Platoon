import { useState } from 'react'

export default function InputWith2Fields(){

    const[inputs, setInputs] = useState({});
    
    // takes 
    const handleChange = (event) =>{
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values,[name]: value}))
    }

    const handleSubmit = (event) =>{
        event.preventDefault();
        alert(inputs)
        console.log(inputs['age'])
        return<p>{inputs['age']} {inputs['value']}</p>
    }

    return(
        <div>
            <h1> 2 fields here </h1>
            <form onSubmit={handleSubmit}>

                <label>Enter Your Name:
                    <input 
                    type="text" 
                    name="username"
                    value={inputs.username || ""}
                    onChange={handleChange}
                    />
                </label>
            
                <label>Enter Your Age:
                    <input 
                    type="number" 
                    name="age"
                    value={inputs.age || ""}
                    onChange={handleChange}
                    />
                </label>
                <input type="submit"/>
            </form>
        </div>
        
    )
}