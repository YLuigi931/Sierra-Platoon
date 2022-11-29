import ArticleList from "../components/ArticleList"
export default function HomePage({articles}){

    return (
        <div>
            This is the home page
             <ArticleList articles={articles}/>
        </div>
    )
}