import React, { Component } from 'react'
import { Divider, List, Pagination } from 'antd';
import './index.css'


export default class CaseList extends Component {
      render() {
            const data = [
                  'Racing car sprays burning fuel into crowd.Japanese princess to wed commoner.Japanese princess to wed commoner.Japanese princess to wed commoner.',
                  'Japanese princess to wed commoner.',
                  'Australian walks 100km after outback crash.',
                  'Man charged over missing wedding girl.',
                  'Los Angeles battles huge wildfires.',
            ];
            return (
                  <div>
                        <Divider className='divider-list' orientation="left">
                              <List
                                    size='small'
                                    split={true}
                                    header={<div className='case-tile'>测试用例列表</div>}
                                    footer={<div ><Pagination className='case-current' defaultCurrent={6} total={10} /></div>}
                                    dataSource={data}
                                    renderItem={
                                          (item) => <List.Item className='list-item'>{item}</List.Item>
                                    }
                              >
                              </List>
                        </Divider>
                  </div>
            )
      }
}
