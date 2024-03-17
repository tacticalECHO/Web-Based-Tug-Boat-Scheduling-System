const { defineConfig } = require('@vue/cli-service')
module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        pathRewrite: {'^/api': '/api'}
      },
    }
  }
};
