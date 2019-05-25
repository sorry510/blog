<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right" class="gm-breadcrumb">
            <el-breadcrumb-item :to="{ path: '/article/category' }">文章分类</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/article/category' }">分类列表</el-breadcrumb-item>
        </el-breadcrumb>
        <el-row :gutter="20">
            <el-col :span="10" style="min-height: 300px; border: 1px solid rgb(209, 227, 229); border-top: 5px solid rgb(209, 227, 229);">
                <el-tree
                    :data="data"
                    node-key="id"
                    :default-expanded-keys="[2, 3]"
                    :default-checked-keys="[5]">
                </el-tree>
            </el-col>
            <el-col :span="14">
              <el-card class="box-card" style="width:100%;">
                <div slot="header" class="clearfix">
                  <span>php[顶级分类]</span>
                    <el-button-group style="float:right">
                        <el-button type="primary" size="small"
                                    ><i class="el-icon-plus"></i>
                            下级分类
                        </el-button>
                        <el-button type="primary" size="small"><i
                                class="el-icon-plus"></i>
                            同级分类
                        </el-button>
                        <el-button type="danger" size="small"> <i class="el-icon-delete"></i></el-button>
                    </el-button-group>
                </div>
                <div>
                   <el-form :model="category" label-position="top" v-if="category.id !=0 " @submit.prevent.native="onSaveClick">
                        <el-form-item label="机构名称" prop="name">
                            <el-input v-model="category.name" placeholder="请输入单位/院系/班级名称"></el-input>
                        </el-form-item>
                        <!--<el-form-item label="排序">-->
                        <!--<el-input-number v-model="category.sort"></el-input-number>-->
                        <!--</el-form-item>-->
                        <el-form-item>
                            <el-button type="primary" @click="onSaveClick" :loading="isSaving">保 存</el-button>
                        </el-form-item>
                    </el-form>
                </div>
              </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
    data() {
      return {
        data: [
          {
            id: 1,
            label: '一级 2',
            children: [{
              id: 3,
              label: '二级 2-1',
              children: [{
                id: 4,
                label: '三级 3-1-1'
              }, {
                id: 5,
                label: '三级 3-1-2',
                disabled: true
            }]
          }, 
          {
            id: 2,
            label: '二级 2-2',
            disabled: true,
            children: [{
              id: 6,
              label: '三级 3-2-1'
            }, {
              id: 7,
              label: '三级 3-2-2',
              disabled: true
            }]
          }]
        }],
        category: {
          id: 1,
          name: '',
        },
        isSaving: false,
      }
    },
    methods: {
      onSaveClick(){

      }
    }
}
</script>
<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
