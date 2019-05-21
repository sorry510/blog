<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="gm-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/form' }">表单</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/form/list' }">表单列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-table
      :data="tableData"
      border
      style="width: 100%" 
      v-loading="loading">
      <el-table-column
        prop="date"
        label="活动时间1"
        >
      </el-table-column>
      <el-table-column
        prop="name"
        label="活动名称"
        >
      </el-table-column>
      <el-table-column
        prop="region"
        label="活动区域"
        >
      </el-table-column>
      <el-table-column
        prop="resource"
        label="活动资源"
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
