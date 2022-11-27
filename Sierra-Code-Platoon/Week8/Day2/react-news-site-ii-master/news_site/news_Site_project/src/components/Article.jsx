
export default function Article({id, title, created_date, url, author, object_id}){
    return (
        <div> 
            <h1>{id}. {title}</h1>
            <a href={url}><p>{url}</p></a> 
            <p> this is more info {title} </p>
            <h5> author: {author} </h5>
            <h5> object: {object_id} </h5>
        </div>
    )
}