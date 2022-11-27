import Article from "./Article";
import {useState} from 'react'

export default function ArticleTeaser({article}){
    //use conditional rendering
    const[showArticle,setShowArticle] = useState(false)

    const renderShowArticle = () =>{
        if(showArticle){
            
            return <Article article={article}/>
        }
    }
    function updateCondition(){
        if(!showArticle){
            setShowArticle(true)
        }else{
            setShowArticle(false)
        }
        
    }

    return (
        <div className="articleTeaser" onClick={updateCondition}>
            <h2>{`${article.id}.  ${article.title} `}</h2>
            <p>{article.created_date}</p>
            {renderShowArticle()}
        </div>
    )
}