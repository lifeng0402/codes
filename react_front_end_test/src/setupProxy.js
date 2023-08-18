
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
      app.use(
            '/api', // 监听的 API 路径
            createProxyMiddleware({
                  target: 'http://127.0.0.1:8000', // 实际接口的地址
                  changeOrigin: true,
                  pathRewrite: { "^/api": "" }
            })
      );
};