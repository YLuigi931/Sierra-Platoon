function Message (props){

    return (
        <div className="message-container">
            <h1> {props.greeting} </h1>
            <p> 
                {/* {displaySubtext()} */}

                {
                props.subtext
                ? props.subtext
                :'no subtext provided'
                }
            </p>
        </div>
    )

}

export default Message