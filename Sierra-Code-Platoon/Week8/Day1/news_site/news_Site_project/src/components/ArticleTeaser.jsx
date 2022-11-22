import { useState } from 'react'
import Article from './Article'

export default function ArticleTeaser({article}){

    const[showArticle, setShowArticle]=useState(false)

    const renderingIfShowArticle = () => {
        if (dataExists) {
          return <Article />
        }
      };

    return (
      <div className='articleTeaser'>
        <div onClick={ ()=> setShowArticle(!showArticle)}>
            <h2>{article.id}. {article.title}</h2>
            <p>{article.created_date}</p>
        </div>  
      {showArticle ? <Article {...article}/> : ''}
    </div>
    )
}