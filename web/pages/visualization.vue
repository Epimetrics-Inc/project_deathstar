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

                    <div class="form-group form-inline vis-type">
                        <label>Coverage</label>
                        <select class="form-control" v-model="coverage">
                            <option value="single">Single Document</option>
                            <option value="all">All Documents</option>
                        </select>
                    </div>
                </div>
                <div class="sidebar-search">
                    <div class="sidebar-search-options">
                        <div class="has-feedback has-feedback-left search-option">
                            <input type="text" class="form-control" placeholder="Search..." />
                            <icon class="form-control-feedback" name="search"></icon>
                        </div>

                        <dropdown>
                            <button data-role="trigger" class="dropdown-toggle btn btn-default search-option" type="button">
                                <icon name="filter"></icon>
                            </button>
                            <template slot="dropdown">
                                <li>
                                    <div class="dropdown-header">
                                        Show only:
                                    </div>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Adolescent Health
                                        </div>
                                    </a>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Geriatric Health
                                        </div>
                                    </a>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            MNCHN
                                        </div>
                                    </a>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Others
                                        </div>
                                    </a>
                                </li>
                                <li class="divider"></li>
                                <li>
                                    <div class="dropdown-header">
                                        Sort by:
                                    </div>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Date (newest)
                                        </div>
                                    </a>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Date (oldest)
                                        </div>
                                    </a>
                                    <a>
                                        <div>
                                            <icon name="check"></icon>
                                            Relevance
                                        </div>
                                    </a>
                                </li>
                            </template>

                        </dropdown>
                    </div>
                </div>
                <transition name="fade">

                    <ul v-if="coverage=='single'" class="nav" id="side-menu">
                        <li v-for="ao in aoDocuments">
                            <a href="/">
                                <div>
                                    <div>{{ ao.docNum }}</div>
                                    <div class="list-title text-muted"> 
                                        {{ ao.docTitle }}
                                    </div>
                                </div>
                            </a>
                        </li>
                    </ul>
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
import 'vue-awesome/icons/plus'
import 'vue-awesome/icons/download'
import 'vue-awesome/icons/search-plus'
import 'vue-awesome/icons/search-minus'

import navheader from '~/components/navheader.vue'
import dropdown from 'uiv/src/components/dropdown/Dropdown.vue'
import collapse from 'uiv/src/components/collapse/Collapse.vue'
import icon from 'vue-awesome/components/Icon'

export default {
  components: {
    navheader,
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
      coverage: 'single',
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
