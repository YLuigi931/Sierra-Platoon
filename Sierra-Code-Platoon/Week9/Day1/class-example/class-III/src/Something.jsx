import { Component } from 'react';

// export default function Something(){
//     return (
//         <div> In Something </div>
//     )
// }


export default class Something extends Component{

    componentDidMount(){
        console.log('component Did Mount: I am alive...')
    }

    componentWillUnmount(){
        console.log('i am being unmounted')
    }

    componentDidUpdate(){
        console.log('I have been updated')
    }


    render(){

        return(
            <div> in something </div>
        )
    }
}