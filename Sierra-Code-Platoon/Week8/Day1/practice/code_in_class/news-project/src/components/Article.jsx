
export default function Article({article}){


    return (
        <div>
            <a href={article.url}>{article.url}</a>
            <a><p>{article.author}</p></a>
            <p>More info here</p>
        </div>
    )
}