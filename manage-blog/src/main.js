import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import './plugins/element.js'
import router from './plugins/router.js'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

window._ = require('lodash')

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
