// Framework
import Vue from 'vue'
import VueRouter from 'vue-router'

// Components
import Timetable from './components/Timetable.vue'
import App from './App.vue'

// Configuration
import routes from "./Routes.vue"
import store from "./store"

Vue.use(VueRouter)
Vue.config.productionTip = false

new Vue({
  // router: new VueRouter({ routes })
  render: f => f(App),
  store
}).$mount('#app')
