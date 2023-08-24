import React, { Component } from 'react';
import { Breadcrumb, Layout, Menu } from 'antd';
import Index from "../Index"
import './index.css';

const { Header, Content, Footer } = Layout;

const moduleNames = [
      { key: 1, label: '首页', content: <Index /> },
      { key: 2, label: '接口测试', content: '接口测试内容' },
      { key: 3, label: '测试项目', content: '测试项目内容' },
      { key: 4, label: '测试用例', content: '测试用例内容' },
      { key: 5, label: '测试报告', content: '测试报告内容' },
      { key: 6, label: '系统设置', content: '系统设置内容' },
];

export default class Project extends Component {
      constructor(props) {
            super(props);

            // 初始状态为首页
            this.state = {
                  selectedModule: 1,
            };
      }

      // 处理模块菜单选择
      handleModuleSelect = ({ key }) => {
            // 更新选中的模块
            this.setState({ selectedModule: key });
      };

      renderModuleContent = () => {
            const { selectedModule } = this.state;
            const selectedModuleInfo = moduleNames.filter(item => item.key === selectedModule)[0];

            return (
                  <div>
                        {selectedModuleInfo ? selectedModuleInfo.content : '模块内容未找到'}
                  </div>
            );
      };

      render() {
            const { selectedModule } = this.state;

            return (
                  <div>
                        <Layout className="layout">
                              <Header className="header">
                                    <div className="demo-logo"></div>
                                    <Menu className="module-names"
                                          theme="dark"
                                          mode="horizontal"
                                          selectedKeys={[selectedModule]}
                                          onSelect={this.handleModuleSelect}
                                          items={moduleNames.map(item => ({ key: item.key, label: item.label }))}>
                                    </Menu>
                              </Header>
                              <Content className="content">
                                    <Breadcrumb className="breadcrumb"
                                          items={[
                                                { title: 'Home' }, { title: <a href="https://www.baidu.com">Application Center</a> }
                                          ]}
                                    />
                                    <div className="site-layout-content">{this.renderModuleContent()}</div>
                              </Content>
                              <Footer className="footer">Debugfeng ©2023 Created by Ddebugfeng.</Footer>
                        </Layout>
                  </div>
            );
      }
}