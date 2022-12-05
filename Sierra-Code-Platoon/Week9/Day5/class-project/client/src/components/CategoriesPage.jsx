import {React, useEffect} from 'react'
import axios from 'axios'
import { useState, useRef } from 'react'



function CategoriesPage() {

  const[categories,setCategories] = useState([]);
  const[titleInput,setTitleInput] = useState('');

  async function getAllCategories(){
    let response = await axios.get('api/categories/')
    console.log(response.data)
    let category_list = response.data.categories
    setCategories(category_list)
  }
  // grabs titleInput and send it to back-end
  async function addCategory(){
    let response = await axios.post('api/categories/',{'title':titleInput})
    console.log(response.data)
    // setCategories(response.data.categories)
  }

  useEffect(() => {
    getAllCategories()
  },[])

  return (
    <div>
      <h1>Categories Page</h1>
      
        {categories.map((category) => (
        
          <h3>{category.title}</h3>
        ))}
          
        <input type='text' placeholder='title' value={titleInput} onChange={(e)=>{setTitleInput(e.target.value)}}/>
        <input type='submit' onClick={addCategory}/>
        <h1>{titleInput}</h1>
    </div>
  )
  
}

export default CategoriesPage