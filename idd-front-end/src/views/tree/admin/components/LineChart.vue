<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import * as echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

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
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    }
    // chartData: {
    //   type: Object,
    //   required: true
    // }
  },
  data() {
    return {
      chart: null,
      mainboard_lack_data: [],
      fan_lack_data: [],
      interface_lack_data: [],
      xAxis_data: [],
      flexible_data:[]
    }
  },
  // watch: {
  //   chartData: {
  //     deep: true,
  //     handler(val) {
  //       this.setOptions(val)
  //     }
  //   }
  // },
  watch: {
      mainboard_lack_data(val) {
        this.mainboard_lack_data = val
        this.initChart();
      }
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
    const url = 'http://127.0.0.1:5003/api/line_chart'
			this.$axios.get(url).then(res => {
        this.mainboard_lack_data = res.data.mainboard_lack_data
        this.fan_lack_data = res.data.fan_lack_data
        this.interface_lack_data = res.data.interface_lack_data
        this.xAxis_data = res.data.xAxis_data
        this.flexible_data = res.data.flexible_data
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
  // methods: {
  //   initChart() {
  //     this.chart = echarts.init(this.$el, 'macarons')
  //     this.setOptions(this.chartData)
  //   },
  //   setOptions({ expectedData, actualData } = {}) {
  //     this.chart.setOption({
  //       xAxis: {
  //         data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  //         boundaryGap: false,
  //         axisTick: {
  //           show: false
  //         }
  //       },
  //       grid: {
  //         left: 10,
  //         right: 10,
  //         bottom: 20,
  //         top: 30,
  //         containLabel: true
  //       },
  //       tooltip: {
  //         trigger: 'axis',
  //         axisPointer: {
  //           type: 'cross'
  //         },
  //         padding: [5, 10]
  //       },
  //       dataZoom: [{
  //         show: false,
  //         height: 30,
  //         xAxisIndex: [
  //           0
  //         ],
  //         bottom: 30,
  //         start: 0,
  //         end: 100,
  //         handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
  //         handleSize: '110%',
  //         handleStyle: {
  //           color: '#d3dee5'
  //         },
  //         textStyle: {
  //           color: '#fff' },
  //         borderColor: '#90979c'

  //       }, {
  //         type: 'inside',
  //         show: true,
  //         height: 15,
  //         start: 1,
  //         end: 35
  //       }],
  //       yAxis: {
  //         axisTick: {
  //           show: false
  //         }
  //       },
  //       legend: {
  //         data: ['expected', 'actual']
  //       },
  //       series: [{
  //         name: 'expected', itemStyle: {
  //           normal: {
  //             color: '#FF005A',
  //             lineStyle: {
  //               color: '#FF005A',
  //               width: 2
  //             }
  //           }
  //         },
  //         smooth: true,
  //         type: 'line',
  //         data: expectedData,
  //         animationDuration: 2800,
  //         animationEasing: 'cubicInOut'
  //       },
  //       {
  //         name: 'actual',
  //         smooth: true,
  //         type: 'line',
  //         itemStyle: {
  //           normal: {
  //             color: '#3888fa',
  //             lineStyle: {
  //               color: '#3888fa',
  //               width: 2
  //             },
  //             areaStyle: {
  //               color: '#f3f8ff'
  //             }
  //           }
  //         },
  //         data: actualData,
  //         animationDuration: 2800,
  //         animationEasing: 'quadraticOut'
  //       }]
  //     })
  //   }
  // }
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.chart.setOption({
        xAxis: {
          // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          data: this.xAxis_data,
          boundaryGap: false,
          axisTick: {
            show: false
          }
        },
        grid: {
          left: 10,
          right: 10,
          bottom: 20,
          top: 30,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          },
          padding: [5, 10]
        },
        dataZoom: [{
          show: false,
          height: 30,
          xAxisIndex: [
            0
          ],
          bottom: 30,
          start: 0,
          end: 100,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle: {
            color: '#d3dee5'
          },
          textStyle: {
            color: '#fff' },
          borderColor: '#90979c'

        }, {
          type: 'inside',
          show: true,
          height: 15,
          start: 1,
          end: 35
        }],
        yAxis: {
          axisTick: {
            show: false
          }
        },
        legend: {
          data: ['主板螺丝缺失', '风扇螺丝缺失','接口未接上','螺丝松动']
        },
        series: [{
          name: '主板螺丝缺失', itemStyle: {
            normal: {
              color: '#FF005A',
              lineStyle: {
                color: '#FF005A',
                width: 2
              }
            }
          },
          smooth: true,
          type: 'line',
          data: this.mainboard_lack_data,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        },
        {
          name: '风扇螺丝缺失',
          smooth: true,
          type: 'line',
          itemStyle: {
            normal: {
              color: '#3888fa',
              lineStyle: {
                color: '#3888fa',
                width: 2
              },
              areaStyle: {
                color: '#f3f8ff'
              }
            }
          },
          data: this.fan_lack_data,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        },
        {
          name: '接口未接上', itemStyle: {
            normal: {
              color: '#228B22',
              lineStyle: {
                color: '#228B22',
                width: 2
              }
            }
          },
          smooth: true,
          type: 'line',
          data: this.interface_lack_data,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        },
         {
          name: '螺丝松动', itemStyle: {
            normal: {
              color: 'purple',
              lineStyle: {
                color: 'purple',
                width: 2
              }
            }
          },
          smooth: true,
          type: 'line',
          data: this.flexible_data,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        }]
      })
    }
  }
  
}
</script>
