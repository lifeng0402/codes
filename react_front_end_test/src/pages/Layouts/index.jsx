import React, { Component } from 'react';
import { Breadcrumb, Layout } from 'antd';
import { Routes, Route } from 'react-router-dom'
import { AppstoreOutlined } from '@ant-design/icons'
import Menus from './Menus';
import Headers from './Headers'
import Cases from '../Cases';
import Index from '../Index';
import Report from '../Report';
import Project from '../Project';
import Interface from '../Interface';
import ReportDetails from '../Report/Details';
import './index.css'


export default class Layouts extends Component {

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
      }

      render() {
            const { modules } = this.state;
            const { onLogout } = this.props; //从父组件中获取回调方法
            return (
                  <div>
                        <Layout>
                              <Headers onLogout={onLogout} />
                              <Layout>
                                    <Layout.Sider className='layout-sider'>
                                          <Menus modules={modules} />
                                    </Layout.Sider>
                                    <Layout className='layout'>
                                          <Breadcrumb
                                                className='layout-breadcrumb'
                                                items={[
                                                      { title: 'Home' }, { title: 'An Application' }
                                                ]}
                                          />
                                          <Layout.Content className='layout-content'>
                                                <Routes>
                                                      <Route path='/cases' element={<Cases />} />
                                                      <Route path='/home' element={<Index />} />
                                                      <Route path='/project' element={<Project />} />
                                                      <Route path='/report' element={<Report />} />
                                                      <Route path='/test' element={<Interface />} />
                                                      <Route path='/report/details' element={<ReportDetails />} />
                                                </Routes>
                                          </Layout.Content>
                                          <Layout.Footer className='layout-footer'>
                                                Debugfeng ©2023 Created by Debugfeng.
                                          </Layout.Footer>
                                    </Layout>
                              </Layout>
                        </Layout>
                  </div>
            )
      }
}



