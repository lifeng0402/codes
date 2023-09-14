import React, { Component } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom'
import Layouts from './pages/Layouts';
import Login from './pages/Login'
import './App.css'


export default class App extends Component {

  state = {
    isAuthenticated: false //登录是否成功状态
  }

  // 更新登录成功状态
  updateIsAuthenticated = (data) => {
    this.setState({ isAuthenticated: data })
  }

  // 更新退出登录状态
  logoutIsAuthenticated = () => {
    this.setState({ isAuthenticated: false })
  }

  render() {
    const { isAuthenticated } = this.state;

    return (
      <div className='app'>
        <Routes>
          <Route path='/login' element={<Login onAuthenticated={this.updateIsAuthenticated} />} />
        </Routes>
        {isAuthenticated ? (<Layouts onLogout={this.logoutIsAuthenticated} />) : (<Navigate to='/login' replace />)}
        {!isAuthenticated && <Navigate to='/login' replace />}
      </div>
    )
  }
}



