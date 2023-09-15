import React, { Component } from 'react'
import { List, Pagination, Button, Modal } from 'antd';
import CaseCreate from '../../../components/CaseCreate';
import './index.css'


export default class CaseList extends Component {

      state = {
            isModalOpen: false,   //是否显示新增用例页面
            isButton: true, //隐藏Send按钮
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
            ]
      }

      handleModal = (value) => {
            this.setState({ isModalOpen: value });
      };

      render() {
            const { caseList, isModalOpen, isButton } = this.state;

            return (
                  <div>
                        <Button className='create-btn' type='primary' onClick={() => this.handleModal(true)}>新增用例</Button>
                        <Modal title="新增测试用例" open={isModalOpen} onCancel={() => this.handleModal(false)} footer={null}
                              wrapClassName="dialog-container" // 添加类名
                        >
                              <div className="dialog-content">
                                    <CaseCreate isButton={isButton} />
                              </div>
                              <div>
                                    <Button className='case-save' type="primary">保存</Button>
                                    <Button className='case-clear' type="primary">清空</Button>
                              </div>
                        </Modal>
                        <div className='list-root'>
                              <List bordered={true} size='small'>
                                    {caseList.map((item, index) => (
                                          <List.Item key={index} actions={[
                                                <Button className="edit-btn" type="primary" ghost>编辑</Button>,
                                                <Button className="del-btn" type="primary" danger>删除</Button>
                                          ]}>
                                                <div className="list-item-content">
                                                      <div className="list-item-title">{item.title}</div>
                                                      <div className="list-item-description">
                                                            <span className="creator">{item.creator}</span>
                                                            &nbsp;&nbsp;&nbsp;
                                                            <span className="create-time">{item.create_time}</span>
                                                      </div>
                                                </div>
                                          </List.Item>
                                    ))}
                              </List>
                        </div>
                        <Pagination className='list-pagination' defaultCurrent={1} total={50} />
                  </div>
            )
      }
}
