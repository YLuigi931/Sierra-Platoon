
import reactLogo from './assets/react.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from 'react-bootstrap/NavBar'
import Nav from 'react-bootstrap/Nav';
import axios from 'axios';
import './App.css';

import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import CategoriesPage from './components/CategoriesPage';
import HomePage from './components/HomePage';
import PostsPage from './components/PostsPage';

function App() {
  

  return (
    <div className="App">
      <h1> World of Kittens </h1>

      <NavBar>
        <Nav.Link href='/'> Home </Nav.Link>
        <Nav.Link href='/categories'> Categories </Nav.Link>
        <Nav.Link href='/posts'> Posts </Nav.Link>
      </NavBar>

      <Router>
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
