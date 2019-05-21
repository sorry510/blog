<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="gm-breadcrumb">
      <el-breadcrumb-item :to="{ path: '/article' }">我的文章</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/article/add' }">新增文章</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="活动名称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="活动区域">
        <el-select v-model="form.region" placeholder="请选择活动区域">
          <el-option label="区域一" value="shanghai"></el-option>
          <el-option label="区域二" value="beijing"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="活动时间">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;" value-format="yyyy-MM-dd"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;" value-format="HH:mm:ss"></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="即时配送">
        <el-switch v-model="form.delivery" active-value="2"
    inactive-value="1"></el-switch>
      </el-form-item>
      <el-form-item label="活动性质">
        <el-checkbox-group v-model="form.type">
          <el-checkbox label="1" name="type">美食/餐厅线上活动</el-checkbox>
          <el-checkbox label="2" name="type">地推活动</el-checkbox>
          <el-checkbox label="3" name="type">线下主题活动</el-checkbox>
          <el-checkbox label="4" name="type">单纯品牌曝光</el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="特殊资源">
        <el-radio-group v-model="form.resource">
          <el-radio label="线上品牌商赞助"></el-radio>
          <el-radio label="线下场地免费"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="活动形式">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit" :loading="isSubmiting">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  //数据表名字form改为active
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
        isSubmiting: false
      }
    },
    created: function() {
      // console.log(this.$data);
      // this.defaultData = JSON.parse(JSON.stringify(this.$data));//深copy一个对象，来去除值不具有JSON 表示形式（数字、字符串、逻辑值、数组、对象、null）的属性，也就是说像undefined和function这样的属性值。
      // console.log(this.defaultData);
    },
    methods: {
      onSubmit() {
        // console.log(this.form)
        this.isSubmiting = true
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