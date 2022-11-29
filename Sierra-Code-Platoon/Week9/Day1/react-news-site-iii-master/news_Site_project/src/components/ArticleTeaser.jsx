import { useState } from 'react'
import Article from './Article'
import {Link, useNavigate} from 'react-router-dom'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

export default function ArticleTeaser({article}){

    const navigate = useNavigate()

    return (
      <div className='articleTeaser'>
        
        <Card style={{ width: '45rem' }}>
          <Card.Body>
            <Card.Title>{article.title}</Card.Title>
            <Card.Text>
              {article.created_date}
            </Card.Text>
            <Button variant="primary" onClick={() => {navigate(`/article/${article.id}`)}}>
              View article page
            </Button>
          </Card.Body>
        </Card>
      
      </div>
    )
    // <div onClick={() => {navigate(`/article/${article.id}`)}}>
    //         {/* <Link to={`/article/${article.id}`}> */}
    //           <h2>{article.id}. {article.title}</h2>
    //         {/* </Link> */}

    //         <p>{article.created_date}</p>
    //     </div>  
}