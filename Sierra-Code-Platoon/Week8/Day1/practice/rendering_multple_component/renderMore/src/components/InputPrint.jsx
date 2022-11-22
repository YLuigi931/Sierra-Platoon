import {useState} from 'react'


export default function InputPrint(){

    const[textArea,setText] = useState(
        "This is the Secret Content for the page"
    );
    
    const changeHandler = (event) =>{
        setText(event.target.value)
    }

    return(
        <div>
            <form>
                {/* textarea is a specific tag */}
                <textarea value={textArea} onChange={changeHandler}/>
            </form>
        </div>
    )
}
