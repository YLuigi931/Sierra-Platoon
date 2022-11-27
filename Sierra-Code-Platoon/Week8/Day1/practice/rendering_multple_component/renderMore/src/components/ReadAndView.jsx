import {useState} from 'react'
import dataNews from '../data/news.json'


export default function ReadAndView(){
    // console.log(dataNews)
    // get the info from the import to our object
    const[allArticles, setAllArticles] = useState(dataNews.map((article,index)=>{
        return{
            id:index+1,
            title:article.title,
            created_date:article.created_at,
            author:article.author,
            object_id:article.objectID
        }
    }));
    console.log(allArticles)
    // now that we know the data is in there
    // next step is to put it on page
    // format of for loop ==>  Object.map( (pointer can be used here) => { logic goes here } )
    // map() only takes in function so use anonymouse functions
    return (
        <div>
            {allArticles.map((article)=>{
                return <p> id:{article.id} -- title:{article.title} -- createdDate:{article.created_date} </p>
            })}
        </div>
    )
    // version when you insert to another component
    // This is inserting to ArticleTeaser component
    // {return(
    //     <div>
    //         {allArticles.map((article)=>{
    //             return <ArticleTeaser id={article.id} title={article.title} createdDate={article.created_date} />
    //         })}
    //     </div>
    // )}
}