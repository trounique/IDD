<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="Title">
        <!-- <template slot-scope="scope">
          {{ scope.row.title }}
        </template> -->
       <span> origin11.jpg</span>
      </el-table-column>
      <el-table-column label="Author" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Pageviews" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.pageviews }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <!-- <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template> -->
        <span>2022-01-27 18:01:50</span>
      </el-table-column>
    </el-table>
    
    
    
    
    
    <!-- <el-table :data="list" style="width: 100%">
			<div v-for="items in tableForm" :key="items.id">
				<el-table-column :label="items.label" :prop="items.prop">
				</el-table-column>
			</div>
			</el-table> -->




  </div>
</template>

<script>
import { getList } from '@/api/table'

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
					label: 'ID',
					prop: "id",
				}, {
					label: '日期',
					prop: "date",
				}, {
					label: '名字',
					prop: "name",
				} ],
      list: [],
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  // mounted() {
	// 		this.$axios.get("api/api/query/all").then(res => {
	// 			this.list = res.data.list
	// 		})
	// 	},
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        this.listLoading = false
      })
    }
  }
}
</script>
