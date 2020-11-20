//<template>
  <div>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>卡片名称</span>
        </div>
        <div  class="text item">
            <input type="text">
        </div>
        </el-card>
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