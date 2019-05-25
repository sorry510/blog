import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
    saveScrollPosition: true,
    routes: [
        {
            path: '*',
            component: () => import('@/components/home/Index.vue'),
        },
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
                    name: 'articleEdit',
                    path: 'edit/:id',
                    component: () => import('@/components/article/Edit.vue'),
                },
                {
                    name: 'articleList',
                    path: 'list',
                    component: () => import('@/components/article/List.vue'),
                },
            ]
        },
        {
            path: '/article/category',
            component: () => import('@/components/articlecategory/List.vue'),
        },
    ],
})