import stateData from '../data/index';
import State from './State';

import {useState} from 'react';
export default function GetData(){
    
    const data = stateData.map((info)=>{
        return{
            state:info.name,
            acro:info['alpha-2'],
        }
    });

    // console.log(data);

    const[open, setOpen] = useState(false);

    const handleOpen = () =>{
        setOpen(!open)
    }
    console.log(open)
    return(
        <div>
            <h4>This are the data</h4>
            <button onClick={handleOpen}> Drop Down </button>
            { open ? (
                    data.map((info) => {
                        return(
                            <button  onClick={ ()=> {alert(`${info.acro}`)}}>
                                <State key={info.acro} state={info.state} abbv={info.acro}/>
                            </button>
                        )
                    })) : null
            }
        </div>
    )
}