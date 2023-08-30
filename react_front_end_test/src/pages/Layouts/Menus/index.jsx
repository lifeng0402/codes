import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'
import { Menu } from 'antd';
import './index.css'


export default class Menus extends Component {

      render() {
            const { modules } = this.props;
            return (
                  <Menu className='menu-modules' defaultSelectedKeys={['1']} mode='inline' theme='dark'>
                        {modules.map((moduleName) => (
                              <Menu.Item key={moduleName.key} icon={moduleName.icon}>
                                    <NavLink to={moduleName.path}>{moduleName.label}</NavLink>
                              </Menu.Item>
                        ))}
                  </Menu>
            )
      }
}
