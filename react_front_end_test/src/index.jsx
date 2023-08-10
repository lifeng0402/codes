import React from 'react';
// 引用ReactDOM
import { createRoot } from 'react-dom/client';
import App from './App';


// 渲染App到页面
const container = document.getElementById("root")
const root = createRoot(container)
root.render(<App />) 