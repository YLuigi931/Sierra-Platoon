import { useState } from 'react'
// import './App.css'
import AppNav from './components/AppNav'
import ArticleTeaser from './components/ArticleTeaser'
import newsData from './data/news.json'
/*
Display: title<h1>, created_at<p>, url<a>, author<p> 
*/

function App() {
  
  // console.log(newsData)

  const [allArticles, setAllArticles] = useState(newsData.map((article, index) => {
    return {
      id: index+1,
      title: article.title,
      created_date: article.created_at,
      url: article.url,
      author: article.author,
      object_id: article.objectID,
    }
  }))
  // console.log(allArticles)
  return (
    <div className='App'>
      <AppNav/>
      {allArticles.map(article => {
        return <ArticleTeaser key={article.id} article={article}/>  
        })}
    </div>
  )
}

export default App
