import Vue from 'vue'
import Router from 'vue-router'
import sy from '@/index/sy'
import register from '@/user/register'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'sy',
      component: sy
    },
    {
      path: '/register',
      name: 'register',
      component: register
    }
  ]
})
