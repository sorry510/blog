<template>
  <div id="app">
    <el-container>
      <el-header>
        <Header></Header>
      </el-header> 
      <el-container>
        <el-aside width="200px">
          <Menu></Menu>
        </el-aside>
        <el-main>
          <keep-alive v-if="$route.meta.keepAlive">
              <router-view></router-view>
          </keep-alive>
          <router-view v-else></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>

import Header from '@/components/layout/Header.vue'
import Menu from '@/components/layout/Menu.vue'

export default {
  name: 'app',
  components: {
    Header,
    Menu,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.el-breadcrumb {
  height: 40px;
}
</style>
<style scoped>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
    padding:0;
  }
  
  .el-aside {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #FFFFFF;
    color: #333;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
