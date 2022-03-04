<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import * as echarts from 'echarts';
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

const animationDuration = 6000

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null,
      mainboard_lack_data:[],
      fan_lack_data:[],
      interface_lack_data:[],
      xAixs_data:[]
    }
  },
watch: {
      mainboard_lack_data(val) {
        this.mainboard_lack_data = val
        this.initChart();
      },
      // fan_lack_data(val) {
      //   this.fan_lack_data = val
      //   this.initChart();
      // },
      // interface_lack_data(val) {
      //   this.interface_lack_data = val
      //   this.initChart();
      // },
      // xAxis_data(val) {
      //   this.xAxis_data_lack_data = val
      //   this.initChart();
      // },
    },

  mounted() {
    const url = "http://127.0.0.1:5003/api/bar_chart"
			this.$axios.get(url).then(res => {
        this.mainboard_lack_data = res.data.mainboard_lack_data
        this.fan_lack_data = res.data.fan_lack_data
        this.interface_lack_data = res.data.interface_lack_data
        this.xAxis_data = res.data.xAxis_data
			})
    this.$nextTick(() => {
      this.initChart()
    })
    
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')

      this.chart.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          top: 10,
          left: '2%',
          right: '2%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: this.xAxis_data,
          axisTick: {
            alignWithLabel: true
          }
        }],
        yAxis: [{
          type: 'value',
          axisTick: {
            show: false
          }
        }],
        series: [{
          name: '主板螺丝缺失',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: this.mainboard_lack_data,
          animationDuration
        }, {
          name: '风扇螺丝缺失',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: this.fan_lack_data,
          animationDuration
        }, {
          name: '接口未接上',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: this.interface_lack_data,
          animationDuration
        }]
      })
    }
  }
}
</script>
