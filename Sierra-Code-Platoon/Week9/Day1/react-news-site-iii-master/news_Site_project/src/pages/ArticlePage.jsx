import { useParams } from "react-router-dom"
import Article from "../components/Article"

export default function ArticlePage({oneArticle}){
    let {articleID} = useParams()
    const article= oneArticle(articleID -1)
    

    return (
        <div>
            <a href='/'>Go Home</a>
            <Article {...article}/>
        </div>
    )
}