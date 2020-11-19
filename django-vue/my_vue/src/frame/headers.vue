<template>
    <el-header style="text-align: right; font-size: 20px">
      <el-dropdown>
        <i style="margin-right: 10px;font-size:20px">用户</i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item><span @click="go_user_info">个人中心</span></el-dropdown-item>
          <el-dropdown-item>注销</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-header>
</template>

<script>
export default {
    mounted(){
        
    },
    methods:{
        go_user_info(){
            this.$router.go("/")
        }
    }
}
</script>

<style>
.el-header {
    background-color: #409EFF;
    color: #333;
    line-height: 60px;
    border-radius: 4px;
    min-height: 180px;
  }
</style>