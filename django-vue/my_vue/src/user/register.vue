//<template>
  <div>
<<<<<<< HEAD
      <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>卡片名称</span>
        </div>
        <div  class="text item">
            <input type="text">
        </div>
        </el-card>
=======
    <el-input v-model="username" placeholder="请输入您的手机号"></el-input>
    <el-input v-model="code" placeholder="请输入短信验证码"></el-input>
    <el-button type="primary" plain>获取短信验证码</el-button>
    <el-input placeholder="请输入您的密码" v-model="password" show-password></el-input>
    <el-button type="primary" plain>注册</el-button>
>>>>>>> 193c2323eb21924becac85453c64ef8cdc4099cb
  </div>
</template>

<script>
export default {

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