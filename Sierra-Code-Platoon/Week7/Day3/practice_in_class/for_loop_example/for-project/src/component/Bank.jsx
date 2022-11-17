
function Bank(props){

    let listOfNames = ['Mario','Luigi','Toad']



    return(
        <div>
            {listOfNames.map(name => {
                return(
                <h4> {name} </h4>
                )
            })}
           
        </div>        
    )
}

export default Bank