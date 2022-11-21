export default function Article({id, title, created_date, url, author, object_id}){

    return(
        <div>
            {/* <a href={url}></a>  */}
            <p> this is more info {title} </p>
            <h5> author: {author} </h5>
            <h5> object: {object_id} </h5>
        </div>
    )
}