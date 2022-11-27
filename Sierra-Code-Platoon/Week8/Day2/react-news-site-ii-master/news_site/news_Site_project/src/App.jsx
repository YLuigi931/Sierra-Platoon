import { useState } from 'react'
import './App.css'
import AppNav from './components/AppNav'
import 'bootstrap/dist/css/bootstrap.min.css';

import newsData from './data/news.json'
import {HashRouter as Router, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import ArticlePage from './pages/ArticlePage'

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
  function getOneArticle(articleID){
    return allArticles[articleID - 1]
  }

  return (
    <div className='App'>
      <AppNav/>

      <Router>
        <Routes>
          <Route path='/' element={<HomePage articles={allArticles}/>}/>
          <Route path='/article/:articleID' element={<ArticlePage oneArticle={getOneArticle}/>}/>
        </Routes>
      </Router>

     
    </div>
  )
}

export default App
