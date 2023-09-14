import React, { Component } from 'react'
import { Select, Input, Tabs, Descriptions, Button } from 'antd';
import ParamsHeaders from './ParamsHeaders';
import BodyRequest from './BodyRequest'
import './index.css'


export default class CaseCreate extends Component {

      state = {
            items: [
                  {
                        value: 'jack',
                        label: 'Jack',
                  },
                  {
                        value: 'disabled',
                        label: 'Disabled',
                        disabled: true,
                  }
            ],
            tabs: [
                  {
                        key: '1',
                        label: `Params`,
                        children: <ParamsHeaders />,
                  },
                  {
                        key: '2',
                        label: `Headers`,
                        children: <ParamsHeaders />,
                  },
                  {
                        key: '3',
                        label: `Body`,
                        children: <BodyRequest />,
                  },
                  {
                        key: '4',
                        label: `Pre-request Script`,
                        children: `Content of Tab Pane 4`,
                  },
                  {
                        key: '5',
                        label: `Test`,
                        children: `Content of Tab Pane 5`,
                  },
            ],
            descriptions: [
                  {
                        key: '10',
                        children: (
                              <>
                                    Data disk type: MongoDB
                                    <br />
                                    Database version: 3.4
                                    <br />
                                    Package: dds.mongo.mid
                                    <br />
                                    Storage space: 10 GB
                                    <br />
                                    Replication factor: 3
                                    <br />
                                    Region: East China 1
                                    <br />
                              </>
                        ),
                  }
            ]
      }

      handleChange = (value) => { console.log(`selected ${value}`); };

      onChange = (key) => { console.log(key); };

      render() {
            const { items, tabs, descriptions } = this.state;
            return (
                  <div>
                        <div className='request'>
                              <Select className='request-method' defaultValue="" onChange={this.handleChange} options={items} />
                              <Input className='request-url' placeholder="https:https://debugfeng.com" />
                        </div>
                        <Tabs defaultActiveKey="1" items={tabs} onChange={this.onChange} />
                        <Descriptions title='Response' bordered items={descriptions} />
                        <Button>保存</Button>
                        <Button>清空</Button>
                  </div>
            )
      }
}
