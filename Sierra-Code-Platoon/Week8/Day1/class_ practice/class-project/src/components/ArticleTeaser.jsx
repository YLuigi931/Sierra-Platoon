import{useState} from 'React'
import Article from './Article'

export default function ArticleTeaser({article}){
    const[showArticle, setShowArticle]= useState(false)

    const renderingIfShowArticle = () =>{
        if(showArticle){
            return <Article/>
        }
    }

    function updateShowArticle(){
        // if(!showArticle){
        //     setShowArticle(true)
        // }else{
        //     setShowArticle(false)
        // }

        // showArticle? setShowArticle(false) : setShowArticle(true)

        setShowArticle(!showArticle)
    }

    return(
        <div className="articleTeaser">
            {/* <div onClick={updateShowArticle()}></div> to call function version*/}
            <div onClick={ () => setShowArticle(!showArticle)}>
                <h2> {article.id}. {article.title} </h2>
                <p>{article.created_date}</p>
            </div>
            {/* conditional rendering example */}
            {/* {showArticle &&
                <Article/>
            } */}
            
            {/* {renderingIfShowArticle()} */}

            {showArticle ? <Article {...article}/> : ''}
            
        </div>
    )


}