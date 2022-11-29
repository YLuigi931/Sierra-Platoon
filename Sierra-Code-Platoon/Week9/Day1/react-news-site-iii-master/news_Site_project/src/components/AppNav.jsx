import labels from '../data/section.json'
import Nav from 'react-bootstrap/Nav';
import Alert from 'react-bootstrap/Alert';

export default function AppNav(){
    return (
        <div>
            <Nav>
            {labels.map((section)=>{
                return (
                    <Nav.Item key={section.label}>
                        <Nav.Link href={`/#/sections/${section.tag}`} key={section.label}>
                            {section.label}
                        </Nav.Link>
                    </Nav.Item>)              
            })}
            </Nav>
        </div>
        
    )
}