import React, { Component } from 'react'
import './index.css'

export default class Item extends Component {

  // 标识：鼠标移入和移出
  state = { mouse: false }

  // 鼠标移入、移出的回调函数
  handleMouse = (flag) => {
    return () => {
      console.log(flag)
      this.setState({ mouse: flag })
    }
  }

  // 勾选、取消勾选某一个todo的回调
  handleCheck = (id) => {
    return (event) => {
      console.log(id)
      this.props.updateTodo(id, event.target.checked)
    }
  }

  handleDelete = (id) => {
    if (window.confirm('确定删除嘛？')) {
      this.props.deleteTodo(id)
    }
    // this.props.deleteTodo(id)

  }

  render() {
    const { id, name, done } = this.props
    const { mouse } = this.state
    return (
      <li style={{ backgroundColor: mouse ? "#ddd" : "white" }} onMouseLeave={this.handleMouse(false)} onMouseEnter={this.handleMouse(true)}>
        <label>
          {/* defaultChecked 第一次默认勾选，可进行修改*/}
          <input type="checkbox" defaultChecked={done} onChange={this.handleCheck(id)} />
          <span>{name}</span>
        </label>
        <button onClick={() => this.handleDelete} className="btn btn-danger" style={{ display: mouse ? "block" : "none" }}>删除</button>
      </li>
    )
  }
}