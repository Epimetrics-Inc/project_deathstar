<template>
    <div id="wrapper">

        <!-- Navigation -->
        <navheader active-sidebar="doc" v-on:tooglesidebar="sidebarCollapse=!sidebarCollapse"></navheader>

        <collapse class="navbar-default navbar-collapse sidebar" v-model="sidebarCollapse">
            <div class="sidebar-nav">
            <navsearch is-doc-active="true" v-on:clickDocument="clickDocument"></navsearch>
            </div>
            <!-- /.sidebar-collapse -->
        </collapse>
            <!-- /.navbar-static-side -->

        <!-- Page Content -->
        <div id="page-wrapper">
            <div class="container-fluid doc-preview" v-if="doc">
                <div class="zoom-buttons">
                    <a id="zoom-out-button" v-on:click="zoomOut()">
                        <icon name="search-minus"></icon>
                    </a>
                    <a id="zoom-in-button" v-on:click="zoomIn()">
                        <icon name="search-plus"></icon>
                    </a>
                </div>
                <div v-bind:style="{fontSize:fontSize + 'px'}" id="zoom-wrapper">
                    <div class="doc-header">
                        <img id="doh-logo" src="../static/doh_logo.png" alt="DOH logo">
                        <div class="header-title">
                            <p>Republic of the Philippines</p>
                            <p>Department of Health</p>
                            <strong>OFFICE OF THE SECRETARY</strong>
                        </div>
                    </div>

                    <br>

                    <div class="doc-date pull-right">
                        {{ doc.date }}
                    </div>

                    <br>

                    <div class="doc-type">
                        {{ doc.doctype }}
                    </div>

                    <div class="doc-num">
                        {{ doc.docnum }}
                    </div>

                    <br>

                    <div class="doc-subject">
                        {{ doc.subject}}
                    </div>

                    <div class="doc-body">
                        {{ doc.body }}
                    </div>

                    <br>
                    <div class="doc-signed pull-right">
                        <div class="doc-sign">
                            {{ doc.sign }}
                            
                        </div>

                        <div class="doc-sign-title">
                            {{ doc.signtitle}}
                        </div>

                    </div>

                    <!-- /.row -->
                </div>
                 <!-- /#zoom-wrapper -->
            </div>
            <!-- /.container-fluid -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->
</template>

<script>
// icon imports
import 'vue-awesome/icons/search-plus'
import 'vue-awesome/icons/search-minus'

import navheader from '~/components/navheader.vue'
import navsearch from '~/components/navsearch.vue'
import collapse from 'uiv/src/components/collapse/Collapse.vue'
import icon from 'vue-awesome/components/Icon'

import { getDocument } from '~/api/api'

export default {
  components: {
    navheader,
    navsearch,
    collapse,
    icon
  },
  head: {
  },

  data: function () {
    return {
      fontSize: 15,
      sidebarCollapse: true,
      doc: false
    }
  },
  methods: {
    zoomIn: function (event) {
      console.log('zoom in')
      if (this.fontSize < 50) { // maximum 50        
        this.fontSize = (this.fontSize + 5)
      }
    },
    zoomOut: function (event) {
      console.log('zoom out')
      if (this.fontSize > 5) { // minimum 5
        this.fontSize = (this.fontSize - 5)
      }
    },
    clickDocument: function (document) {
      getDocument(document).then(res => {
        this.doc = res.data
      })
    }
  }
}
</script>

<style>
/*Start of Document Preview*/

#doh-logo{
  float:left;
}

#page-wrapper .doc-preview{
  background-color: #FFFFFF;
  padding:50px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  font-family: Garamond,serif;
  word-wrap: break-word;
}

#page-wrapper .header-title {
  text-align: center;
  margin: auto;
  width: 80%;
  padding: 10px;
  font-size:20px;
}

#page-wrapper .header-title > p {
  margin:0;
}

#page-wrapper .doc-subject{
  font-weight:bold;
}

#page-wrapper .doc-body{
  white-space: pre-line;
}

#page-wrapper .doc-sign{
  font-weight:bold;
}

#page-wrapper .doc-signed .doc-sign-title{
  text-align:center;
}



/*End of Document Preview*/

</style>
