<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/article' }">我的文章</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/article/list' }">文章列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-table
      :data="articleList"
      border
      style="width: 100%" 
      v-loading="loading">
      <el-table-column
        prop="title"
        label="标题"
        >
      </el-table-column>
      <el-table-column
        prop="category_name"
        label="标签"
        >
      </el-table-column>
      <el-table-column
        prop="update_time"
        label="修改时间"
        >
      </el-table-column>
      <el-table-column
        prop="views"
        label="访问人数"
        >
      </el-table-column>
      <el-table-column
        label="操作"
        >
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="edit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="del(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import { getArticleList } from '@/api/article'
  export default {
    data() {
      return {
        articleList: [],
        loading: false,
      }
    },
    created() {
      this.init()
    },
    methods: {
      init() {
        this.loading = true
        getArticleList()
          .then(res=> {
            this.loading = false
            console.log(res)
            // console.log(res[1])
            this.articleList = res
          })
          .catch(err=> {
            this.loading = false
            console.log(err)
          })
      },
      edit(index, row) {
        this.$router.push({
          path: `/article/edit/${row.id}`, 
        })
      },
      del() {

      }
    }
  }
</script>
<style type="text/css">

</style>
