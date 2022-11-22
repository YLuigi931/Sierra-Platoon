import { useState } from 'react'

export default function(){

    
    const numbers = [1,2,3,4,5,6];
    const listItems = numbers.map((numbers) =>
        <li>{numbers}</li>    
    );
    return(
        <ul> {listItems} </ul>
    )
}