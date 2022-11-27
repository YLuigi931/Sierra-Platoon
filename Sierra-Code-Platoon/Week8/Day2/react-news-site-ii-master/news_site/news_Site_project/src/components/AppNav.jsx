import labels from '../data/section.json'
import Nav from 'react-bootstrap/Nav';

export default function AppNav(){
    return (
        <div>
            <Nav>
            {labels.map((section)=>{
                return (
                    <Nav.Item>
                        <Nav.Link onClick={()=> alert("You clicked " + section.label)}>
                        {section.label}
                        </Nav.Link>
                    </Nav.Item>)              
            })}
            </Nav>
        </div>
        
    )
}