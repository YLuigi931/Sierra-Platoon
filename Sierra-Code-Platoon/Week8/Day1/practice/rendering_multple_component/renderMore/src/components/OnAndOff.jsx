import { useState } from 'react'


function OnAndOff(){
    const[press, setPress] = useState(true);

    const onImage = <img src={window.location.origin + '/src/assets/on.svg'} />
    const offImage = <img src={window.location.origin + '/src/assets/off.svg'} />

    function buttonPress(){
        if (press === true){
            setPress(false)
        } else{
            setPress(true)
        }
    }   
    console.log(press)
    return(
        <div>
            <button onClick={buttonPress} > Click me </button>
            <div>
                {press ? onImage : offImage}
            </div>
            
        </div>
    )
}
export default OnAndOff;