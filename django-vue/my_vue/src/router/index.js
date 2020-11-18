import Vue from 'vue'
import Router from 'vue-router'
import sy from '@/index/sy'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'sy',
      component: sy
    }
  ]
})
