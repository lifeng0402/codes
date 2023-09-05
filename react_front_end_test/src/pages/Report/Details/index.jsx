import React, { Component } from 'react';
import { Collapse } from 'antd';
import { Descriptions } from 'antd';


const text = `
  A dog is a type of domesticated animal.
  Known for its loyalty and faithfulness,
  it can be found as a welcome guest in many households across the world.
`;

export default class ReportDetails extends Component {

      state = {
            items: [
                  {
                        key: '1',
                        label: 'This is panel header 1',
                        children: <p>{text}</p>,
                  },
                  {
                        key: '2',
                        label: 'This is panel header 2',
                        children: <p>{text}</p>,
                  },
                  {
                        key: '3',
                        label: 'This is panel header 3',
                        children: <p>{text}</p>,
                  },
                  {
                        key: '4',
                        label: 'This is panel header 3',
                        children: <p>{text}</p>,
                  },
                  {
                        key: '5',
                        label: 'This is panel header 3',
                        children: <p>{text}</p>,
                  },
            ],
            descriptions: [
                  {
                        key: '1',
                        label: '报告名称',
                        children: '自动化测试报告',
                  },
                  {
                        key: '2',
                        label: '用例总数',
                        children: '8888',
                  },
                  {
                        key: '3',
                        label: '通过率',
                        children: '52%',
                  },
                  {
                        key: '4',
                        label: '用例失败数',
                        children: '55555',
                  },
                  {
                        key: '5',
                        label: '用例成功数',
                        children: '555',
                  },
                  {
                        key: '6',
                        label: '用例错误数',
                        children: '55',
                  },
            ]
      }

      onChange = (key) => { console.log(key); }

      render() {
            const { items, descriptions } = this.state;
            return (
                  <div>
                        <Descriptions title="报告详情页面" items={descriptions} />
                        <div>
                              <label>测试用例运行详情</label>
                        </div>
                        <Collapse items={items} onChange={this.onChange} />
                  </div>
            )
      }
}
