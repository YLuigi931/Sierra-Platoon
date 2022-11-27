import ArticleTeaser from "./ArticleTeaser"

export default function ArticleList({articles}) {

    return (
        <div className="Article-List">
            <p>Article List Here</p>
            {articles.map(article => {
                return <ArticleTeaser key={article.id} article={article}/>  
            })}
        </div>
    )
}