
import sections from '../data/section.json'

export default function AppNav(){

    return(
        <div> 
            <nav>
                {sections.map(section => {
                    return (<p onClick={ ()=> alert('You have Clicked ' + section.label)}>
                    {section.label}
                    </p>)
                })}
            </nav>
        </div>
    )
}