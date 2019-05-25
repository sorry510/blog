import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import './plugins/element.js'
import router from './plugins/router.js'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

window._ = require('lodash')

import { mockXHR } from '@/mock/index'
if (process.env.NODE_ENV !== 'production') {
  mockXHR()
}

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
