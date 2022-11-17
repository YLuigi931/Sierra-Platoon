import { Component } from "react";

export default class ClassMessage extends Component{
    constructor(){
        super()
        this.state = {
            count:0,
            something: 'something'
        }
    }
    render(){

        return(
            <div>
                <h1>greeting: {this.props.greeting} </h1>
                <p>
                    {
                        this.props.subtext
                        ? this.props.subtext
                        : 'no subtext provided'
                    }
                </p>
            </div>
        )

    }
}