import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Login from "./components/Login";
import Register from "./components/Register";
import './App.css';


export default class App extends Component {

  render() {
    return (
      <Router>
        <div className='container'>
          <Login/>
          {/* <h2>Which body of water?</h2>
          <nav>
            <ul>
              <li>
                <Link to="/register">
                  <code>/register</code>
                </Link>
              </li>
              <li>
                <Link to="/login">
                  <code>/login</code>
                </Link>
              </li>
            </ul>
          </nav>

          <Routes>
            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />
          </Routes> */}
        </div>
      </Router>
    )
  }
}



