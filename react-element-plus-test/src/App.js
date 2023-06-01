import React, { Component } from 'react';
import Header from './components/Header';
import List from './components/List';
import Footer from './components/Footer';
import './App.css'

// 创建并暴露App组件
export default class App extends Component {
  // 状态在哪里，操作状态的方法就在哪里

  // 初始化数据
  state = {
    todos: [
      { id: "1", name: "吃饭", done: true },
      { id: "2", name: "睡觉", done: true },
      { id: "3", name: "敲代码", done: false },
    ]
  }

  // 用于添加一个todo，接收的参数是todo对象
  addTodo = (todoObj) => {
    console.log("APP", todoObj);
    // 获取原理的todos
    const { todos } = this.state
    // 追加一个todo
    const newTodos = [todoObj, ...todos]
    // 更新状态
    this.setState({ todos: newTodos })
  }

  // updateTodo用于更新一个todo对象
  updateTodo = (id, done) => {
    // 获取状态中的todos
    const { todos } = this.state
    // 匹配处理数据
    const newTodos = todos.map((todoObj) => {
      if (todoObj.id === id) return { ...Object, done }
      else return todoObj
    })
    this.setState({ todos: newTodos })
  }

  // deleteTdo用于删除一个todo对象
  deleteTodo = (id) => {
    // 获取原来的todos
    const { todos } = this.state
    // 删除指定ID的todo对象
    const newTodos = todos.filter((todoObj) => {
      return todoObj.id !== id
    })
    // 更新状态
    this.setState({ todos: newTodos })
  }

  render() {
    const { todos } = this.state
    return (
      <div className="todo-container">
        <div className="todo-wrap">
          <Header addTodo={this.addTodo} />
          <List todos={todos} updateTodo={this.updateTodo} deleteTodo={this.deleteTodo} />
          <Footer />
        </div>
      </div >
    )
  }
}