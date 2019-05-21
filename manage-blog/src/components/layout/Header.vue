<template>
   <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item index="2"><a href="#" target="_blank">退出</a></el-menu-item>
        <el-submenu index="1">
            <template slot="title">admin</template>
            <el-menu-item index="1-1">修改信息</el-menu-item>
            <el-menu-item index="1-2">修改密码</el-menu-item>
        </el-submenu>
    </el-menu>
</template>
<style scoped>
    /*.el-menu--horizontal>.el-submenu {
        float: right;
    } */
    ul.el-menu > li {
        float: right;
    } 
</style>
