// 配置lodash依赖于webpack插件
const webpack = require('webpack')
module.exports = {
    baseUrl: './',
    productionSourceMap: false,
    // 全局配置lodash
    // configureWebpack: {
    //     plugins: [
    //       new webpack.ProvidePlugin({
    //         _:"lodash"   
    //         })
    //     ]
    // },
    devServer: {
        proxy: {
            // 以 /api 开头的url请求 都会被拦截 替换为: target/api
            '^/api':{
                target:'http://localhost:8000',
                changeOrigin:true
            },
        }
    }
}