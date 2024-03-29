import React, { Component } from 'react'
import { SearchOutlined } from '@ant-design/icons';
import { Input, Space, DatePicker, Button } from 'antd';
import './index.css'


export default class SearchTerms extends Component {
      render() {
            return (
                  <div>
                        <Space className='space-search'>
                              <Input className='case-name' size='large' placeholder="用例名称" />
                              <Input className='case-create' size='large' placeholder="创建人" />
                              <DatePicker.RangePicker className='case-select-time' placeholder={["开始时间", "结束时间"]} />
                        </Space>
                        <Space wrap direction="horizontal">
                              <Button className='select-btn' type='primary' icon={<SearchOutlined />}>
                                    查询
                              </Button>
                              <Button className='rest-btn' type='primary'>重置</Button>
                        </Space>
                  </div>
            )
      }
}
