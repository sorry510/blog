import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
    saveScrollPosition: true,
    routes: [
        // {
        //     path: '/article/add',
        //     component: () => import('../components/article/Add.vue'),
        // },
        {
            path: '/article',
            component: () => import('@/components/layout/Middle.vue'),
            redirect:'/article/list',
            children: [
                {
                    name: 'articleAdd',
                    path: 'add',
                    component: () => import('@/components/article/Add.vue'),
                    // meta: {
                    //     keepAlive: true
                    // }
                },
                {
                    path: 'list',
                    name: 'articleList',
                    component: resolve => import('@/components/article/List.vue')
                },
            ]
        }
    ],
})