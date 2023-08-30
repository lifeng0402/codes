import React, { Component } from 'react';
import { AppstoreOutlined } from '@ant-design/icons'
import { Routes, Route, Navigate } from 'react-router-dom'
import Layouts from './pages/Layouts';
import Login from './pages/Login'
import './App.css'


export default class App extends Component {

  state = {
    modules: [
      { key: '1', path: '/home', label: '首页', icon: <AppstoreOutlined /> },
      { key: '2', path: '/test', label: '接口测试', icon: <AppstoreOutlined /> },
      { key: '3', path: '/project', label: '项目管理', icon: <AppstoreOutlined /> },
      { key: '4', path: '/cases', label: '用例管理', icon: <AppstoreOutlined /> },
      { key: '5', path: '/report', label: '测试报告', icon: <AppstoreOutlined /> },
      { key: '6', path: '/continue', label: '持续集成', icon: <AppstoreOutlined /> },
      { key: '7', path: '/setting', label: '系统设置', icon: <AppstoreOutlined /> },
    ],
    caseList: [
      {
        title: 'Racing car spanese princess to wed commoner.Japanese princess to wed commoner.Australian walks 100km after outback crash.',
        creator: 'debugfeng',
        create_time: '2023-08-30'
      },
      {
        title: 'Japanese princess to wed commoner.',
        creator: 'debugfeng',
        create_time: '2023-08-30'
      },
      {
        title: 'Australian walks 100km after outback crash.',
        creator: 'debugfeng',
        create_time: '2023-08-30'
      },
      {
        title: 'Los Angeles battles huge wildfires.',
        creator: 'debugfeng',
        create_time: '2023-08-30'
      },
    ],
    isAuthenticated: false
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
    const { modules, caseList, isAuthenticated } = this.state;

    return (
      <div>
        <Routes>
          <Route path='/login' element={<Login onAuthenticated={this.updateIsAuthenticated} />} />
        </Routes>
        {isAuthenticated ? (
          <Layouts modules={modules} caseList={caseList} onLogout={this.logoutIsAuthenticated} />
        ) : (
          <Navigate to='/login' replace />
        )}
        {!isAuthenticated && <Navigate to='/login' replace />}
      </div>
    )
  }
}



