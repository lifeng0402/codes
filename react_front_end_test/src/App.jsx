import React, { Component } from 'react'
import Login from "./components/Login"
import Register from "./components/Register"
import './App.css'


export default class App extends Component {

  render() {
    return (
      <div className='app-container'>
        {/* <Login /> */}
        <Register/>
      </div>

    )
  }
}



