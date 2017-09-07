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
                    <div class="form-group form-inline">
                        <label>Coverage</label>
                        <select class="form-control" v-model="coverage">
                            <option value="single">Specific Document</option>
                            <option value="theme">Specific Theme</option>
                            <option value="all">All Documents</option>
                        </select>
                    </div>
                    <transition name="fade">
                    <div class="form-group form-inline" v-show="coverage=='theme'">
                      <label>Themes</label>
                      <select class="form-control">
                          <option>Adolescent Health</option>
                          <option>Geriatric Health</option>
                          <option>MNCHN</option>
                          <option>Special Population</option>
                      </select>
                		</div>
                		</transition>
                </div>
		        		
		        		<transition name="fade">
        					<navsearch is-doc-active="false" v-show="coverage=='single'"></navsearch>
								</transition>
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
import collapse from 'uiv/src/components/collapse/Collapse.vue'
import icon from 'vue-awesome/components/Icon'

export default {
  components: {
    navheader,
    navsearch,
    collapse,
    icon
  },
  data: function () {
    return {
      sidebarCollapse: true,
      coverage: 'single'
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
