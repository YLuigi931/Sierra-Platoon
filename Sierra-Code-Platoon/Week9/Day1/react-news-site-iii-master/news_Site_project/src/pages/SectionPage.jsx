import { useState, useContext } from "react"
import {useParams} from 'react-router-dom'

import {ArticlesContext} from '../App'
import ArticleList from "../components/ArticleList";

export default function SectionPage(){

    const {tagID} = useParams();
    const articles= useContext(ArticlesContext);

    function getFilterArticles(){
        let filteredList = articles.filter( (article) => {
            // console.log(article)
            for(let tag of article.tags){
                if(tag === tagID){
                    return true
                }
            }
        }); 
        console.log(filteredList)
        return filteredList
    }

    

    return(
        <div>
            This is the section page {tagID}

            <ArticleList articles={getFilterArticles()}/>
        </div>
    )
}