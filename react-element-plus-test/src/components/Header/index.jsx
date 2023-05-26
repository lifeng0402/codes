import React, { Component } from 'react'
import './index.css'
import { nanoid } from 'nanoid'

export default class Header extends Component {

  handleKeyUp = (event) => {
    // 解构赋值获取keyCode, target
    const { keyCode, target } = event
    // 判断是否是回车键
    if (keyCode !== 13) return
    // 添加的todo名称不能为空
    if (target.value.trim() === "") {
      alert("输入不能为空")
      return
    }
    // 准备一个todo对象
    const todoObj = { id: nanoid(), name: target.value, done: false }
    // 将addTodo里传递给App
    this.props.addTodo(todoObj)
    // console.log(event)
    target.value = ""
  }

  render() {
    return (
      <div className='todo-header'>
        <input onKeyUp={this.handleKeyUp} type="text" placeholder="请输入你的任务名称, 按回车键确认" />
      </div>
    )
  }
}
