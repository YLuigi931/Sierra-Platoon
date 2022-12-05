
import reactLogo from './assets/react.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from 'react-bootstrap/NavBar'
import Nav from 'react-bootstrap/Nav';
import axios from 'axios';
// import './App.css';

import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import CategoriesPage from './components/CategoriesPage';
import HomePage from './components/HomePage';
import PostsPage from './components/PostsPage';

function App() {
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');
  axios.defaults.headers.common["X-CSRFToken"]=csrftoken

  return (
    <div className="App">
      <h1> World of Kittens </h1>
      
      <Router>
      <NavBar>
        {/* <Nav.Link href='/'> Home </Nav.Link>
        <Nav.Link href='/categories'> Categories </Nav.Link>
        <Nav.Link href='/posts'> Posts </Nav.Link> */}
        <Link to='/'> router link Home </Link>
        <Link to='/categories'> router link categories</Link>
        <Link to='/posts'> reouter link posts</Link>
      </NavBar>

        <Routes>
          <Route path='' element={<HomePage/>}/>
          <Route path='categories/' element={<CategoriesPage/>}/>
          <Route path='posts/' element={<PostsPage/>}/>
        </Routes>
      </Router>

    </div>
  )
}

export default App
