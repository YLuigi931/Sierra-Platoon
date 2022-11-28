import './App.css';
import { useState, useEffect } from "react";
import Something from './components/Something';

function App() {

  const [titles, setTitles] = useState(null)
  const [makeAPI, setMakeAPI] = useState(false)

  // useEffect is called when the functional component has mounted and when certain state data is updated
  useEffect(() => {
    if (makeAPI) { // the makeAPI state variable is initially FALSE
      getPhotosAPI()
    }
  }, [makeAPI]) // useEffect will only execute again if the makeAPI variable changes

  // getTitles functions sets the makeAPI state variable to TRUE
  const getTitles = () => {
    setMakeAPI(true)
  }

  // Makes a Fetch request to the API and then sets the returned data to state 'titles'
  const getPhotosAPI = async () => {
    let response = await fetch('https://jsonplaceholder.typicode.com/photos')
    let data = await response.json()
    setTitles(data)
  }

  // showTitle function accepts the titles state as an argument and maps through
  const showTitles = (titles) => {
    console.log(titles)
    let articleTitles = []
    titles.map((title, index) => {
      return articleTitles.push(
        <div key={index}>
        <img src={title.thumbnailUrl} alt={`color-${index}`}/>
        <p >{title.title}</p>
        </div>
        )
    })
    return articleTitles
  }

  return (
    <div className="App">
      <h1>Using the useEffect Hook</h1>
      {
        titles
        ?
        <h2>Finished Loading</h2>
        :
        <div>No Titles</div>
      }
      {
        titles && <div>{showTitles(titles)}</div>
      }
      <div>
        <button onClick={getTitles}>Get Titles</button>
      </div>
    </div>
  );
}

export default App;