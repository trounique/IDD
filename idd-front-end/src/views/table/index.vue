<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      id="exportTab"
      border
      fit
      highlight-current-row
    >
    <div v-for="(info,index) in tableForm" :key="index">
        <el-table-column
          :property="info.prop"
          :label="info.label"
          align="center" 
          width="135"
          height="50"
          v-if="index != 0"
         >
         <template slot-scope="scope">
            {{scope.row[scope.column.property]}} 
         </template>
        </el-table-column>

        <el-table-column 
          :label="info.label" 
          v-if="index == 0" 
          :property="info.prop"
          width="167px">
        <template slot-scope="scope">
          <el-image :src="scope.row[info.prop]"
          :preview-src-list="[scope.row[info.prop]]" 
          width="40px" height="40" align="center" />
        </template>
          </el-table-column>

    </div>
    <!-- <el-table-column
          v-for="(info,index) in tableForm"
          :key="index"
          :property="info.prop"
          :label="info.label"
          align="center" 
          width="140"
         >
         <template slot-scope="scope">
                   {{scope.row[scope.column.property]}}  
              </template>
    </el-table-column> -->

    </el-table>
    
    
    
    
    
    <!-- <el-table :data="list" style="width: 100%">
			<div v-for="items in tableForm" :key="items.id">
				<el-table-column :label="items.label" :prop="items.prop">
				</el-table-column>
			</div>
			</el-table> -->



  <el-button type="primary" style="background-color: #0086b3" @click="exportExcel">导出</el-button>
  </div>
  
</template>

<script>
// import { getList } from '@/api/table'
import FileSaver from 'file-saver'
import XLSX from 'xlsx'
export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableForm: [{
					label: '点击查看结果',
					prop: "draw_url",
				}, {
					label: 'ID',
					prop: "id",
				}, {
					label: '日期',
					prop: "date",
				}, {
					label: '名字',
					prop: "name",
				} , {
					label: '主板螺丝完好数目',
					prop: "mainboard_good",
				}, {
					label: '主板螺丝缺失数目',
					prop: "mainboard_lack",
				}, {
					label: '风扇螺丝完好数目',
					prop: "fan_good",
				}, {
					label: '风扇螺丝缺失数目',
					prop: "fan_lack",
				}, {
					label: '接口正确接上数目',
					prop: "interface_good",
				}, {
					label: '接口没有接上数目',
					prop: "interface_lack",
				},
        {
					label: '螺丝松动',
					prop: "flexible",
				},
        {
					label: '是否合格',
					prop: "qval",
				}
        ],
      list: [],
      srcList: [],
      listLoading: true
    }
  },
  created() {
    this.listLoading = false
    const url = "http://127.0.0.1:5003/api/query/all"
			this.$axios.get(url).then(res => {
				this.list = res.data.list
        this.srcList = res.data.srcList;
			})
  },
  // mounted() {
    
	// 	},
  methods: {
  //   fetchData() {
  //     this.listLoading = true
  //     getList().then(response => {
  //       this.list = response.data.items
  //       this.listLoading = false
  //     })
  //   }
  exportExcel () {
	/* generate workbook object from table */
	 //表名
	 var wb = XLSX.utils.table_to_book(document.querySelector('#exportTab'))
	 /* get binary string as output */
	 var wbout = XLSX.write(wb, { bookType: 'xlsx', bookSST: true, type: 'array' })
	 try {
	   FileSaver.saveAs(new Blob([wbout], { type: 'application/octet-stream' }), '分析表.xlsx')
	 } catch (e) { if (typeof console !== 'undefined') console.log(e, wbout) }
	 return wbout
},
  }
}
</script>
