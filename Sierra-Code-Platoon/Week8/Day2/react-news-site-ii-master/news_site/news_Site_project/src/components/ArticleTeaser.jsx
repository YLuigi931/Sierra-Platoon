import { useState } from 'react'
import Article from './Article'
import {Link, useNavigate} from 'react-router-dom'

export default function ArticleTeaser({article}){

    const navigate = useNavigate()

    return (
      <div className='articleTeaser'>
        <div onClick={() => {navigate(`/article/${article.id}`)}}>
            {/* <Link to={`/article/${article.id}`}> */}
              <h2>{article.id}. {article.title}</h2>
            {/* </Link> */}

            <p>{article.created_date}</p>
        </div>  
      
    </div>
    )
}