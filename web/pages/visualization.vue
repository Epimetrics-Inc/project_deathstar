<template>
    <div id="wrapper">

        <!-- Navigation -->	
        <navheader isVisActive="true" v-on:tooglesidebar="sidebarCollapse=!sidebarCollapse"></navheader>
    		<collapse class="navbar-default navbar-collapse sidebar" v-model="sidebarCollapse">
            <div class="sidebar-nav">
                
                <div class="sidebar-vis-options">
                    <div class="form-group form-inline vis-type">
                        <label>Type</label>
                        <select class="form-control">
                            <option>Word Cloud</option>
                            <option>Frequency Chart</option>
                        </select>
                    </div>
                </div>
		        		
        				<navsearch is-doc-active="false"></navsearch>

                <div>
                    <button class="btn btn-default visualize-button" href="#" type="button">
                        Visualize
                    </button>
                </div>
            </div>
            <!-- /.sidebar-collapse -->
        </collapse>
            <!-- /.navbar-static-side -->
        <!-- Page Content -->
        <div id="page-wrapper">
            <div class="container-fluid">

            </div>
            <!-- /.container-fluid -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->
</template>

<script>
import 'vue-awesome/icons/search'
import 'vue-awesome/icons/filter'
import 'vue-awesome/icons/check'

import navheader from '~/components/navheader.vue'
import navsearch from '~/components/navsearch.vue'
import dropdown from 'uiv/src/components/dropdown/Dropdown.vue'
import collapse from 'uiv/src/components/collapse/Collapse.vue'
import icon from 'vue-awesome/components/Icon'

export default {
  components: {
    navheader,
    navsearch,
    dropdown,
    collapse,
    icon
  },
  data: function () {
    return {
      aoDocuments: [
        {
          docNum: 'AO No. 2017-0001-A',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-B',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-C',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-D',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-E',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-F',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-G',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-H',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-I',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        },
        {
          docNum: 'AO No. 2017-0001-J',
          docTitle: 'Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings'
        }
      ],
      filters: [
        'Adolescent Health',
        'Geriatric Health',
        'MNCHN',
        'Special Population'
      ],
      checkedAOs: [],
      checkedFilters: {},
      sortBy: 'newest',
      sidebarCollapse: true
    }
  },
  methods: {
    selectAll: function (event) {
      for (let ao of this.aoDocuments) {
        this.checkedAOs.push(ao.docNum)
      }
    },
    deselectAll: function (event) {
      this.checkedAOs = []
    },
    toggleFilter: function (filter) {
      if (this.checkedFilters[filter]) {
        this.checkedFilters[filter] = false
      } else if (this.checkedFilters[filter] === false) {
        this.checkedFilters[filter] = true
      } else {
        this.$set(this.checkedFilters, filter, true)
      }
    },
    setSortBy: function (sort) {
      this.sortBy = sort
    }
  }
}
</script>

<style>
/*Start of Visualisation Sidebar*/
.sidebar .sidebar-vis-options {
  margin-bottom: 0;
}

.sidebar .sidebar-vis-options *:last-child{
  margin-bottom:0;
}

.sidebar .sidebar-vis-options .form-group > label {
  width:28%;
}

.sidebar .sidebar-vis-options .form-group > select {
  width:70%;
}

.sidebar .visualize-button{
  float:right;
}
/*End of Visualisation Sidebar*/
</style>
