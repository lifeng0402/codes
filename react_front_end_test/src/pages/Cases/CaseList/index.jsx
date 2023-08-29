import React, { Component } from 'react'
import { Button, Space, Pagination } from 'antd'
// import { Divider, List, Pagination } from 'antd';
import './index.css'


export default class CaseList extends Component {
      render() {
            const data = [
                  'Racing car spanese princess to wed commoner.',
                  'Japanese princess to wed commoner.',
                  'Australian walks 100km after outback crash.',
                  'Man charged over missing wedding girl.',
                  'Los Angeles battles huge wildfires.',
                  'Racing car spanese princess to wed commoner.',
                  'Japanese princess to wed commoner.',
                  'Australian walks 100km after outback crash.',
                  'Man charged over missing wedding girl.',
                  'Los Angeles battles huge wildfires.',
            ];
            return (
                  <div>
                        <div className='list-border'>
                              {data.map((item, index) => (
                                    <div key={index} className='list-div'>
                                          <dl className='list-item'>
                                                <dt>{item}</dt>
                                          </dl>
                                          <Space wrap className='list-button'>
                                                <Button className='edit-btn' type='primary' ghost>编辑</Button>
                                                <Button className='del-btn' type='primary' danger>删除</Button>
                                          </Space>
                                    </div>
                              ))}
                        </div>
                        <Pagination className='list-pagination' defaultCurrent={1} total={50} />
                  </div>
            )
      }
}
