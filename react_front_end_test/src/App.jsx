import React, { Component } from 'react';
import Login from "./pages/Login";
import Manage from './pages/Manage';
import './App.css'


export default class App extends Component {

  state = {
    moduleNames: [
      { key: '1', path: '/home', label: '首页' },
      { key: '2', path: '/test', label: '接口测试' },
      { key: '3', path: '/project', label: '项目管理' },
      { key: '4', path: '/cases', label: '用例管理' },
      { key: '5', path: '/report', label: '测试报告' },
      { key: '6', path: '/continue', label: '持续集成' },
      { key: '7', path: '/setting', label: '系统设置' },
    ]

  }


  render() {
    const { moduleNames } = this.state;
    return (
      <div>
        <Manage moduleNames={moduleNames} />
        {/* <Login /> */}
      </div>
    )
  }
}



