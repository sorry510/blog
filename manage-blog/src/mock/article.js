import Mock from 'mockjs'
// const Random = Mock.Random;
const articleList = Mock.mock({
    "array|5-10": [{
        'id|+1': 1,
        'title': '@ctitle(10, 30)',
        'category_name': '@ctitle(4)',
        'update_time': '@date("yyyy-MM-dd")',
        'views': '@integer(1, 10000)'
    }]
})

export default [
    {
        url: '/api/article/list',
        type: 'get',
        response: articleList['array']
    },
    {
        url: /\/api\/article\/edit\/\d+/,
        type: 'get',
        response: {
            'id': '@integer(1, 10)',
            'title': '@ctitle(10, 30)',
            'summary': '@csentence(30, 50)',
            'body': '@cparagraph(5, 10)',
            'category_id': '@integer(1, 5)',
            'is_public': '@integer(0, 1)',
            'img': '@image()'
        }
    }
]