import React, { Component } from 'react'
import { Button } from 'antd'
import { List, Pagination } from 'antd';
import './index.css'


export default class CaseList extends Component {
      render() {
            const { caseList } = this.props;
            return (
                  <div>
                        <Button className='create-btn' type='primary'>新增用例</Button>
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
