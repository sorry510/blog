import request from '@/api/request'

//这里是获取文章列表
export function getArticleList(data){
  return request ({
    url: '/api/article/list',
    method:'get',
    data
  })
}
//查看文章
export function preview(data, id){
  return request({
    url: `/api/article/edit/${id}`,
    method:'get',
    data
  })
}
//删除文章
export function deleteArticle(data){
  return request({
    url:'/api/article/del',
    method:'post',
    data
  })
}
//编辑文章
export function editArticle(data){
  return request ({
    url: '/api/article/edit',
    method: 'post',
    data
  })
}
//新增文章
export function addArticle(data){
  return request ({
    url: '/api/article/add',
    method: 'post',
    data
  }) 
}
