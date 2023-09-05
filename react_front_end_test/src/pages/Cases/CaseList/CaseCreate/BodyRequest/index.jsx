import React, { Component } from 'react'
import { Tabs, Select, Input } from 'antd';
import ParamsHeaders from '../ParamsHeaders';


export default class BodyRequest extends Component {

      state = {
            tabs: [
                  {
                        key: '1',
                        label: 'none',
                        children: '',
                  },
                  {
                        key: '2',
                        label: 'from-data',
                        children: <ParamsHeaders />,
                  },
                  {
                        key: '3',
                        label: 'x-www-from-urlencoded',
                        children: <ParamsHeaders />,
                  },
                  {
                        key: '4',
                        label: 'raw',
                        children: <Input style={{ height: 120 }} />,
                  },
                  {
                        key: '5',
                        label: 'binary',
                        children: 'Content of Tab Pane 5',
                  },
                  {
                        key: '6',
                        label: 'GraphQL',
                        children: 'Content of Tab Pane 6',
                  }
            ],
            opts: [
                  {
                        value: 'jack',
                        label: 'Json',
                  },
                  {
                        value: 'lucy',
                        label: 'JavaScript',
                  },
                  {
                        value: 'Yiminghe',
                        label: 'Text',
                  },
                  {
                        value: 'disabled',
                        label: 'HTML',
                  },
                  {
                        value: 'disableds',
                        label: 'XML',
                  }
            ],
            isRawSelected: false,
      }

      onChange = (key) => { console.log(key); };

      isRawOnChange = (key) => {
            if (key === '4' || key === '6') {
                  // 当选择 "raw" 选项卡时，将 isRawSelected 设置为 true
                  this.setState({ isRawSelected: true });
            } else {
                  this.setState({ isRawSelected: false });
            }
      };

      render() {
            const { tabs, isRawSelected, opts } = this.state;
            return (
                  <div>
                        <Tabs defaultActiveKey="1" items={tabs} onChange={this.isRawOnChange} tabBarExtraContent={(
                              isRawSelected && (
                                    <Select bordered={false} options={opts} style={{ width: 120, marginRight: 330 }} />
                              )
                        )} />

                  </div>
            )
      }
}
