<template>
    <div id="wrapper">

        <!-- Navigation -->	
        <navheader isVisActive="true" v-on:tooglesidebar="sidebarCollapse=!sidebarCollapse"></navheader>
    		<collapse class="navbar-default navbar-collapse sidebar" v-model="sidebarCollapse">
            <div class="sidebar-nav">
                
                <div class="sidebar-vis-options">
                    <div class="form-group form-inline">
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
      sidebarCollapse: true
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
