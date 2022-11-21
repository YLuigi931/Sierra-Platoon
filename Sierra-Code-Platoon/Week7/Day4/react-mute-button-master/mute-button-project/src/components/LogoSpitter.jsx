import { useState } from 'react'

function LogoSpitter(){
    const [check, setCheck] = useState(true);
    
    function buttonPress(){
        
        if(check === false){
            setCheck(true)
        }else{
            setCheck(false)
        }
               
    }
    // check ?
    // check = false: check = true 

    // console.log(check)

    //     let imgName =  check ?
    const onImage = <img src={window.location.origin + '/on.svg'} />
    const offImage = <img src={window.location.origin + '/off.svg'} />

    return(
        <div>
        
        <button onClick={buttonPress} > Change the Logo </button>
        <div>{ check ? onImage : offImage}</div>
        </div>
    )
}

export default LogoSpitter;