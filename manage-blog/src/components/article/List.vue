<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/article' }">我的文章</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/article/list' }">文章列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-table
      :data="tableData"
      border
      style="width: 100%" 
      v-loading="loading">
      <el-table-column
        prop="date"
        label="标题"
        >
      </el-table-column>
      <el-table-column
        prop="name"
        label="标签"
        >
      </el-table-column>
      <el-table-column
        prop="region"
        label="修改时间"
        >
      </el-table-column>
      <el-table-column
        prop="resource"
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
  export default {
    data() {
      return {
        tableData: [
          
        ],
        loading: true,
      }
    },
    created() {
      this.init()
    },
    methods: {
      init() {
        this.tableData = [
          {
            date: '2018-09-09',
            name: 'hello',
            region: 'beijing',
            resource: 'wu'
          }
        ]
        this.loading = false
        // axios.get('/form/list', {
        //   params: {

        //   }
        // })
        // .then((response) => {
        //   this.loading = false
        //   // log(response.data)
        //   this.tableData = response.data
        // })
        // .catch((error) => {

        // })
      },
      edit(index, row) {
        this.$router.push({
          path: '/form/edit/'+row.active_id, 
        })
      },
      del() {

      }
    }
  }
</script>
<style type="text/css">

</style>
