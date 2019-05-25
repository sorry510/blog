<template>
    <el-menu :router="true">
        <el-submenu index="1" :router="true">
            <template slot="title"><i class="el-icon-menu"></i>我的文章</template>
            <el-menu-item index="/article/add">新增文章</el-menu-item>
            <el-menu-item index="/article/list">文章列表</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>文章分类</template>
                <el-menu-item index="/article/category">分类列表</el-menu-item>
                <!-- <el-menu-item index="/article/category/list">分类列表</el-menu-item> -->
        </el-submenu>
        <el-submenu index="3">
            <template slot="title"><i class="el-icon-menu"></i>评论设置</template>
                <el-menu-item index="3-1">文章评论</el-menu-item>
        </el-submenu>
        <el-submenu index="4">
            <template slot="title"><i class="el-icon-menu"></i>文章审核</template>
                <el-menu-item index="4-1">审核列表</el-menu-item>
        </el-submenu>
        <el-submenu index="5">
            <template slot="title"><i class="el-icon-menu"></i>统计报表</template>
                <el-menu-item index="5-1">综合统计</el-menu-item>
        </el-submenu>
        <el-submenu index="6">
            <template slot="title"><i class="el-icon-menu"></i>其他设置</template>
                <el-menu-item index="6-1">添加标签</el-menu-item>
                <el-menu-item index="6-2">文章列表</el-menu-item>
        </el-submenu>
    </el-menu>
</template>

<style scoped>
.el-menu {
    background-color: #E9EEF3;
}
.el-submenu .el-menu {
    background-color: rgb(228, 238, 241);
}
</style>

