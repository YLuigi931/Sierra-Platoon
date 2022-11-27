import { useState } from 'react'
import ArticleTeaser from './components/ArticleTeaser'
import AppNav from './components/AppNav'
import './App.css'

import newsData from'./data/news.json'


function App() {
  
  // console.log(newsData)
  // if we are assembling a new output make sure to return it use {} brackets
  const[allArticles,setAllArticles] = useState(newsData.map((article, index)=>{
    // the left corner is what we like to name it
    // the right corner is how we reference the data from the file
    return{
      id: index+1,
      title: article.title,
      created_date: article.created_at,
      url: article.url,
      author: article.author,
      object_id: article.objectID
    }
  }))
  // console.log(allArticles)
  return (
    <div className="App">
      <AppNav/>
      {/* for loop in return using "map" */}
      {/* refer to the already assembled result */}
      {allArticles.map((article)=>{
        return <ArticleTeaser key={article.id} article={article}/>
      })}
      
    </div>
  )
}

export default App
