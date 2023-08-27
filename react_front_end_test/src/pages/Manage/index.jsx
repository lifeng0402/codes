import React from 'react';
import { Breadcrumb, Layout, Menu, Button } from 'antd';
import { NavLink, Route, Routes } from 'react-router-dom';
import Index from '../Index';
import Cases from '../Cases';
import Integration from '../Integration';
import Report from '../Report';
import Settings from '../Settings';
import Interface from '../Interface';
import Project from '../Project';
import HeaderTitle from '../../components/HeaderTitle';
import './index.css'

const { Header, Content, Sider, Footer } = Layout;


export default class Manage extends React.Component {
      render() {
            const { moduleNames } = this.props;
            return (
                  <div>
                        <Layout className='layou-demo'>
                              <Header className='demo-header'>
                                    <HeaderTitle />
                                    <div className='logout-btn'>
                                          <Button type='dashed' ghost>退出登录</Button>
                                    </div>
                              </Header>
                              <Layout>
                                    <Sider className='demo-sider'>
                                          <Menu className='demo-sider-menu' mode="inline" defaultSelectedKeys={['1']} defaultOpenKeys={['1']}>
                                                {moduleNames.map((module) => (
                                                      <Menu.Item key={module.key}>
                                                            <NavLink activeClassName='debugfeng' className='list-group-item' to={module.path}>{module.label}</NavLink>
                                                      </Menu.Item>
                                                ))}
                                          </Menu>
                                    </Sider>
                                    <Layout className='demo-layout'>
                                          <Breadcrumb items={[{ title: <a href='https://www.baidu.com'>/百度一下</a> }]} />
                                          <Content>
                                                <Routes>
                                                      <Route path='/home' element={<Index />} />
                                                      <Route path='/cases' element={<Cases />} />
                                                      <Route path='/test' element={<Interface />} />
                                                      <Route path='/project' element={<Project />} />
                                                      <Route path='/report' element={<Report />} />
                                                      <Route path='/continue' element={<Integration />} />
                                                      <Route path='/setting' element={<Settings />} />
                                                </Routes>
                                          </Content>
                                          <Footer className='demo-footer'>
                                                Debugfeng ©2023 Created by Debugfeng.
                                          </Footer>
                                    </Layout>
                              </Layout>
                        </Layout>
                  </div>
            )
      }
}
