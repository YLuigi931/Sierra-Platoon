import dataMenu from '../data/section.json'
import Nav from 'react-bootstrap/Nav';
export default function AppNav(){

    

// 1d array
    return (
        <div className=''>
            <h3> This is Nav </h3>
            <Nav>
                {dataMenu.map((column)=>{
                    return (<Nav.Item>
                                <Nav.Link onClick={()=>{ alert('you click ' + column.label)}}>
                                    {column.label}
                                </Nav.Link>
                        </Nav.Item>)
                })}
            </Nav>
        </div>  
    )
}