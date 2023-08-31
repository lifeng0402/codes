import React, { Component } from 'react'
import { Select, Input, Tabs, Descriptions, Button } from 'antd';


export default class CaseCreate extends Component {

      state = {
            items: [
                  {
                        value: 'jack',
                        label: 'Jack',
                  },
                  {
                        value: 'lucy',
                        label: 'Lucy',
                  },
                  {
                        value: 'Yiminghe',
                        label: 'yiminghe',
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
                        label: `Tab 1`,
                        children: `Content of Tab Pane 1`,
                  },
                  {
                        key: '2',
                        label: `Tab 2`,
                        children: `Content of Tab Pane 2`,
                  },
                  {
                        key: '3',
                        label: `Tab 3`,
                        children: `Content of Tab Pane 3`,
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
                  <div className="dialog-content">
                        <Select defaultValue="" style={{ width: 120, }} onChange={this.handleChange} options={items} />
                        <Input placeholder="Basic usage" />
                        <Tabs defaultActiveKey="1" items={tabs} onChange={this.onChange} />
                        <Descriptions title='Response' bordered items={descriptions} />
                        <Button>保存</Button>
                        <Button>清空</Button>
                        {/* 对话框的内容 */}
                        {/* <p>some contents...</p>
                        <p>some contents...</p>
                        <p>some contents...</p> */}
                  </div>
            )
      }
}
