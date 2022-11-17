import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import ClassMessage from './component/classMessage'
import Message from './component/Message'

function App() {
  const [messages, setMessages] = useState(['hey','hello','how are you'])

  function display100(){
    let newMessages = []
    for(let i =0; i<100; i++){
      newMessages.push(<Message key={`${i}`} greeting={`this is message ${i}`}/>);
    }
    return (
      <div>
        {array}
      </div>
    );
  }

}
//   return (
//     <div className="App">
//       <Bank/>
//       <h1> ----------------------------------------</h1>
//       <ClassMessage greeting="class component greeting" ></ClassMessage>
//       render()
//       {newMessages}

//       <h1> ----------------------------------------</h1>
      
//     </div>
//   )
// }

export default App;