import ArticleTeaser from "./ArticleTeaser"
// import { useContext } from 'react'
// import { ArticlesContext } from '../App'

export default function ArticleList({articles}) {

    // const articlesFromContext = useContext(ArticlesContext)

    return (
        <div className="Article-List">
            
            {articles.map(article => {
                return <ArticleTeaser key={article.id} article={article}/>  
            })}

            {/* { articlesFromContext.map( (article) => {
                return <ArticleTeaser key={article.id} article={article}/>
            })} */}
           
        </div>
    )
}