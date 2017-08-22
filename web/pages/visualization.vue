<template>
    <div id="wrapper">

        <!-- Navigation -->
        <navheader isVisActive="true"></navheader>

        <div class="navbar-default sidebar navbar-collapse" role="navigation">
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
                            <select class="form-control">
                                <option>Single Document</option>
                                <option>All Documents</option>
                            </select>
                        </div>
                    </div>
                    <div class="sidebar-search">
                        <div class="sidebar-search-options">
                            <div class="has-feedback has-feedback-left search-option">
                                <input type="text" class="form-control" placeholder="Search..." />
                                <i class="form-control-feedback glyphicon glyphicon-search"></i>
                            </div>

                            <div class = "dropdown">
                                <button class="dropdown-toggle btn btn-default search-option" data-toggle="dropdown" href="#" type="button">
                                    <i class="glyphicon glyphicon-filter"></i>
                                </button>
                                <ul class="dropdown-menu dropdown-options">
                                    <li>
                                        <div class="dropdown-header">
                                            Show only:
                                        </div>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
                                                Adolescent Health
                                            </div>
                                        </a>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
                                                Geriatric Health
                                            </div>
                                        </a>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
                                                MNCHN
                                            </div>
                                        </a>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
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
                                                <i class="glyphicon glyphicon-ok"></i>
                                                Date (newest)
                                            </div>
                                        </a>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
                                                Date (oldest)
                                            </div>
                                        </a>
                                        <a>
                                            <div>
                                                <i class="glyphicon glyphicon-ok"></i>
                                                Relevance
                                            </div>
                                        </a>
                                    </li>
                                </ul>

                            </div>
                        </div>
                    </div>
                    <ul class="nav" id="side-menu">
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li href="index.html">
                            <a href="index.html">
                                <div>
                                    <div>AO No. 2017-0001-A</div>
                                    <div class="list-title text-muted"> 
                                        Policy Guidelines on the Standards of Care for Older Persons in All Healthcare Settings
                                    </div>
                                </div>
                            </a>
                        </li>
                    </ul>

                    <div>
                        <button class="btn btn-default visualize-button" href="#" type="button">
                            Visualize
                        </button>
                    </div>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
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
import navheader from '~/components/navheader.vue'

export default {
  components: {
    navheader
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
