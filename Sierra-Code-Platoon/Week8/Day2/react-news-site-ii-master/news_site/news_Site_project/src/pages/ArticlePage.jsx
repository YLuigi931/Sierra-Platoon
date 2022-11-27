import { useParams } from "react-router-dom"
import Article from "../components/Article"

export default function ArticlePage({oneArticle}){
    let {articleID} = useParams()
    const article= oneArticle(articleID)
    

    return (
        <div>
            <Article {...article}/>
        </div>
    )
}