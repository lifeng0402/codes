// 引入核心库
import React from 'react';
// 引用ReactDOM
import { createRoot } from 'react-dom/client';
// import ReactDOM from 'react-dom';
// 引用组件
import App from './App';

// 渲染App到页面
const container = document.getElementById("root")
const root = createRoot(container)
root.render(<App tab="home"/>) 