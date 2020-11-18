//<template>
  <div>
    <!-- 头部区域 -->
    <headers></headers>
    <el-button>Cilck in</el-button>
    <!-- 足部区域 -->
    <footer></footer>
  </div>
</template>

<script>

import headers from '../frame/headers.vue'
import footer from '../frame/footer.vue'
export default {
  components:{
    headers,
    footer
  }
}
</script>

<style>

</style>