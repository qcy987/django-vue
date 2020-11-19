//<template>
  <div>
    <el-input v-model="username" placeholder="请输入您的手机号"></el-input>
    <el-input v-model="code" placeholder="请输入短信验证码"></el-input>
    <el-button type="primary" plain>获取短信验证码</el-button>
    <el-input placeholder="请输入您的密码" v-model="password" show-password></el-input>
    <el-button type="primary" plain>注册</el-button>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>