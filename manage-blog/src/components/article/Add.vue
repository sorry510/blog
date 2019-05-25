<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="gm-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/article' }">我的文章</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/article/add' }">新增文章</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="文章分类">
        <!-- <el-select v-model="form.region" placeholder="请选择类别">
          <el-option label="区域一" value="shanghai"></el-option>
          <el-option label="区域二" value="beijing"></el-option>
        </el-select> -->
        <el-cascader
          placeholder="试试搜索：指南"
          :options="options"
          filterable
          change-on-select
        ></el-cascader>
      </el-form-item>
      <el-form-item label="文章标题">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="文章简介">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="是否发布">
        <el-switch v-model="form.delivery" active-value="2"
    inactive-value="1"></el-switch>
      </el-form-item>
      <el-form-item label="活动形式">
        <mavon-editor v-model="form.desc" ref="md" @imgAdd="imgAdd" style="min-height: 600px"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit" :loading="isSubmiting">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  //数据表名字form改为active
  import { mavonEditor } from 'mavon-editor'
  import 'mavon-editor/dist/css/index.css'
  export default {
    data() {
      return {
        form: {
          form_id: 0,
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        options: [{
          value: 'zhinan',
          label: '指南',
          children: [{
            value: 'shejiyuanze',
            label: '设计原则',
            children: [{
              value: 'yizhi',
              label: '一致'
            }, {
              value: 'fankui',
              label: '反馈'
            }, {
              value: 'xiaolv',
              label: '效率'
            }, {
              value: 'kekong',
              label: '可控'
            }]
          }, {
            value: 'daohang',
            label: '导航',
            children: [{
              value: 'cexiangdaohang',
              label: '侧向导航'
            }, {
              value: 'dingbudaohang',
              label: '顶部导航'
            }]
          }]
        }, {
          value: 'zujian',
          label: '组件',
          children: [{
            value: 'basic',
            label: 'Basic',
            children: [{
              value: 'layout',
              label: 'Layout 布局'
            }, {
              value: 'color',
              label: 'Color 色彩'
            }, {
              value: 'typography',
              label: 'Typography 字体'
            }, {
              value: 'icon',
              label: 'Icon 图标'
            }, {
              value: 'button',
              label: 'Button 按钮'
            }]
          }, {
            value: 'form',
            label: 'Form',
            children: [{
              value: 'radio',
              label: 'Radio 单选框'
            }, {
              value: 'checkbox',
              label: 'Checkbox 多选框'
            }, {
              value: 'input',
              label: 'Input 输入框'
            }, {
              value: 'input-number',
              label: 'InputNumber 计数器'
            }, {
              value: 'select',
              label: 'Select 选择器'
            }, {
              value: 'cascader',
              label: 'Cascader 级联选择器'
            }, {
              value: 'switch',
              label: 'Switch 开关'
            }, {
              value: 'slider',
              label: 'Slider 滑块'
            }, {
              value: 'time-picker',
              label: 'TimePicker 时间选择器'
            }, {
              value: 'date-picker',
              label: 'DatePicker 日期选择器'
            }, {
              value: 'datetime-picker',
              label: 'DateTimePicker 日期时间选择器'
            }, {
              value: 'upload',
              label: 'Upload 上传'
            }, {
              value: 'rate',
              label: 'Rate 评分'
            }, {
              value: 'form',
              label: 'Form 表单'
            }]
          }, {
            value: 'data',
            label: 'Data',
            children: [{
              value: 'table',
              label: 'Table 表格'
            }, {
              value: 'tag',
              label: 'Tag 标签'
            }, {
              value: 'progress',
              label: 'Progress 进度条'
            }, {
              value: 'tree',
              label: 'Tree 树形控件'
            }, {
              value: 'pagination',
              label: 'Pagination 分页'
            }, {
              value: 'badge',
              label: 'Badge 标记'
            }]
          }, {
            value: 'notice',
            label: 'Notice',
            children: [{
              value: 'alert',
              label: 'Alert 警告'
            }, {
              value: 'loading',
              label: 'Loading 加载'
            }, {
              value: 'message',
              label: 'Message 消息提示'
            }, {
              value: 'message-box',
              label: 'MessageBox 弹框'
            }, {
              value: 'notification',
              label: 'Notification 通知'
            }]
          }, {
            value: 'navigation',
            label: 'Navigation',
            children: [{
              value: 'menu',
              label: 'NavMenu 导航菜单'
            }, {
              value: 'tabs',
              label: 'Tabs 标签页'
            }, {
              value: 'breadcrumb',
              label: 'Breadcrumb 面包屑'
            }, {
              value: 'dropdown',
              label: 'Dropdown 下拉菜单'
            }, {
              value: 'steps',
              label: 'Steps 步骤条'
            }]
          }, {
            value: 'others',
            label: 'Others',
            children: [{
              value: 'dialog',
              label: 'Dialog 对话框'
            }, {
              value: 'tooltip',
              label: 'Tooltip 文字提示'
            }, {
              value: 'popover',
              label: 'Popover 弹出框'
            }, {
              value: 'card',
              label: 'Card 卡片'
            }, {
              value: 'carousel',
              label: 'Carousel 走马灯'
            }, {
              value: 'collapse',
              label: 'Collapse 折叠面板'
            }]
          }]
        }, {
          value: 'ziyuan',
          label: '资源',
          children: [{
            value: 'axure',
            label: 'Axure Components'
          }, {
            value: 'sketch',
            label: 'Sketch Templates'
          }, {
            value: 'jiaohu',
            label: '组件交互文档'
          }]
        }],
        isSubmiting: false
      }
    },
    components: {
      mavonEditor
    },
    created: function() {
      // console.log(this.$data);
      // this.defaultData = JSON.parse(JSON.stringify(this.$data));//深copy一个对象，来去除值不具有JSON 表示形式（数字、字符串、逻辑值、数组、对象、null）的属性，也就是说像undefined和function这样的属性值。
      // console.log(this.defaultData);
    },
    methods: {
      imgAdd(pos, $file) {
        var formdata = new FormData();
        formdata.append('file', $file);
        // 这里没有服务器供大家尝试，可将下面上传接口替换为你自己的服务器接口
        this.$axios({
            url: '/common/upload',
            method: 'post',
            data: formdata,
            headers: { 'Content-Type': 'multipart/form-data' },
        }).then((url) => {
            this.$refs.md.$img2Url(pos, url);
        })
      },
      onSubmit() {
        // console.log(this.form)
        // this.isSubmiting = true
        // axios.post('/form/add', this.form)
        // .then((response) => {
        //   // console.log(JSON.stringify(response.data));
        //   // console.log(response.data);
        //   this.isSubmiting = false
        //   if (response.data.code == 0) {
        //     this.$message({
        //         title: '提示',
        //         message: response.data.msg,
        //         type: 'success'
        //     });
        //     Object.assign(this.$data, this.$options.data())//重置data
        //     // window.location='/#/form/add'
        //     // this.$data = Object.assign({}, this.defaultData)//es6深层复制对象
        //   } else {
        //      this.$message({
        //         title: '提示',
        //         message: response.data.msg,
        //         type: 'warning'
        //     });
        //   }
        // })
        // .catch((error) => {
        //   console.log(error)
        // })
      }
    }
  }
</script>