<template>
  <div class="search-wrapper">
    <div class="sidebar-search">
        <div class="sidebar-search-options">
            <div class="has-feedback has-feedback-left search-option">
                <input type="text" class="form-control" placeholder="Search..." v-model.lazy="searchString"/>
                <icon class="form-control-feedback" name="search"></icon>
            </div>
            <button class=" btn btn-default search-option icon-button" type="button" v-on:click="isFilterModalOpen=true" id="filter-button">
                <icon name="filter"></icon>
            </button>
            <div v-if="isDocActive == 'true'">
                <button class=" btn btn-default search-option icon-button" type="button" id="upload-button">
                    <icon name="plus"></icon>
                </button>
            </div>
        </div>
        
        <transition name="fade">
            <div id = "export-options" v-show="checkedAOs.length > 0">
                <button v-on:click="selectAll()" class="btn btn-default selector-button" type="button">
                    Select all
                </button>
                <button v-on:click="deselectAll()" class="btn btn-default selector-button" href="#" type="button">
                    Deselect all
                </button>
                    <button v-on:click="downloadDocs()" v-if="isDocActive == 'true'" class="btn btn-default search-option export-button icon-button" type="button">
                        <icon name="download"></icon>
                    </button>
            </div>
        </transition>
    </div>
    <ul class="nav document-list" id="side-menu">
        <li v-for="ao in aoDocuments" :key="ao.pk">
            <a v-on:click="clickDocument(ao.pk)">
                <div class="list-checkbox">
                    <input v-bind:value="ao.pk" type="checkbox" v-model="checkedAOs">
                </div>
                <div>
                    <div>{{ ao.doctype }} {{ ao.docnum}}</div>
                    <div class="list-title text-muted"> 
                        <!-- {{ ao.docTitle }} -->
                        {{ ao.date }} //will contain the subject
                    </div>
                </div>
            </a>
        </li>
    </ul>

    <pagination v-model="currentPage" :total-page="totalPage" :max-size="maxSize" :size="'sm'" :boundary-links="true" :direction-links="false"></pagination>

    <modal v-model="isFilterModalOpen" title="Search options" class="modal-wrapper">
        <div class="modal-custom-header">Themes</div>
        <div id="filter-themes">
            <label class="checkbox-inline" v-for="filter in filters">
                <input type="checkbox" v-bind:value="filter" v-model="checkedFilters">
                {{ filter }}
            </label>
        </div>

        <hr>

        <div class="modal-custom-header">Sort by</div>
        <div id="filter-sort">
            <label class="radio-inline">
                <input type="radio" v-model="sortBy" value = "newest">
                Date (newest)
            </label>
            <label class="radio-inline">
                <input type="radio" v-model="sortBy" value = "oldest">
                Date (oldest)
            </label>
            <label class="radio-inline">
                <input type="radio" v-model="sortBy" value = "relevance">
                Relevance
            </label>
        </div>
        
        <hr>
        <div class="modal-custom-header">Date signed</div>
        <div class="form-inline">
            <!-- datefrom dropdown + date-picker -->
            <dropdown class="form-group" id="filter-date-from">
                <label for="datefrom">From </label>
                <div class="input-group" id="datefrom">
                    <input class="form-control" type="text" v-model.lazy="dateFrom">
                    <div class="input-group-btn">
                        <button class="btn btn-default" type="button" data-role="trigger">
                            <icon name="calendar"></icon>
                        </button>
                    </div>
                </div>
                <template slot="dropdown">
                    <li>
                        <date-picker v-model="dateFrom" :today-btn="false" :clear-btn="false" class="datepicker"></date-picker>
                    </li>
                </template>
            </dropdown>
            <!--/ datefrom dropdown + date-picker -->
            
            <!-- dateto dropdown + date-picker -->
            <dropdown class="form-group" id="filter-date-from">
                <label for="dateTo">To: </label>
                <div class="input-group" id="dateto">
                    <input class="form-control" type="text" v-model.lazy="dateTo">
                    <div class="input-group-btn">
                        <button class="btn btn-default" type="button" data-role="trigger">
                            <icon name="calendar"></icon>
                        </button>
                    </div>
                </div>
                <template slot="dropdown">
                    <li>
                        <date-picker v-model="dateTo" :today-btn="false" :clear-btn="false" class="datepicker"></date-picker>
                    </li>
                </template>
            </dropdown>
            <!--/ dateto dropdown + date-picker -->
        </div>
        <hr>

        <div class="modal-custom-header">Signed by</div>
        <div>
          <input class="form-control" type="text" v-model="signedBy">

        </div>
    </modal>
    <div class="overlay" v-show="isLoading">
      <icon name="spinner" pulse></icon>
    </div>
  </div>
</template>

<script>
// icon imports
import 'vue-awesome/icons/search'
import 'vue-awesome/icons/filter'
import 'vue-awesome/icons/check'
import 'vue-awesome/icons/plus'
import 'vue-awesome/icons/download'
import 'vue-awesome/icons/calendar'
import 'vue-awesome/icons/spinner'

import dropdown from 'uiv/src/components/dropdown/Dropdown.vue'
import modal from 'uiv/src/components/modal/Modal.vue'
import pagination from 'uiv/src/components/pagination/Pagination.vue'
import icon from 'vue-awesome/components/Icon.vue'

import datePicker from '~/components/datepicker/DatePicker.vue'
import { getDocuments } from '~/api/api'

export default {
  components: {
    dropdown,
    modal,
    datePicker,
    pagination,
    icon
  },
  data: function () {
    return {
      aoDocuments: [],
      filters: [
        'Adolescent Health',
        'Geriatric Health',
        'MNCHN',
        'Special Population'
      ],
      checkedAOs: [],
      checkedFilters: [],
      sortBy: 'relevance',
      isFilterModalOpen: false,
      dateFrom: '',
      dateTo: '',
      signedBy: '',
      searchString: '',
      currentPage: 1, // used for pagination
      maxSize: 4, // used for pagination
      totalPage: 0, // used for pagination
      isLoading: false
    }
  },
  props: ['isDocActive'],
  methods: {
    selectAll: function (event) {
      for (let ao of this.aoDocuments) {
        this.checkedAOs.push(ao.pk)
      }
    },
    deselectAll: function (event) {
      this.checkedAOs = []
    },
    downloadDocs: function (event) {
      this.deselectAll()
      alert('Document download')
    },
    validateDate: function (dateObjectName) {
      var date = new Date(this[dateObjectName])
      var year
      var month
      var day

      if (isNaN(date)) {
        this[dateObjectName] = ''
      } else {
        month = '' + (date.getMonth() + 1)
        day = '' + date.getDate()
        year = date.getFullYear()

        if (month.length < 2) {
          month = '0' + month
        }
        if (day.length < 2) {
          day = '0' + day
        }

        this[dateObjectName] = [year, month, day].join('-')
      }
    },
    clickDocument: function (document) {
      this.$emit('clickDocument', document)
    },
    queryGetDocuments: function (query) {
      this.isLoading = true

      getDocuments(query).then(res => {
        this.isLoading = false
        this.aoDocuments = res.data.results
        this.totalPage = Math.ceil(parseInt(res.data.count) / 10)
      }).catch(function (error) {
        this.isLoading = false
        // TODO: fix error handling
        error({ statusCode: 500, message: 'can\'t fetch data' })
      })
    }
  },
  watch: {
    searchString: function () {
      this.queryGetDocuments({search: this.searchString})
    },
    dateFrom: function () {
      this.validateDate('dateFrom')
    },
    dateTo: function () {
      this.validateDate('dateTo')
    },
    currentPage: function () {
      this.maxSize = this.currentPage >= 995 ? 3 : 4 // update max size
      this.queryGetDocuments({page: this.currentPage, search: this.searchString})
    }
  },
  mounted: function () {
    for (let filter of this.filters) { // initialize to check all filters
      this.checkedFilters.push(filter)
    }
    this.queryGetDocuments()
  }
}
</script>

<style>
.sidebar-nav .search-wrapper{
  margin: 0px;
  height: inherit;
  display: flex;
  flex-direction: column;
  min-height: 50px;
}

.search-wrapper > div{
  margin-right:15px;
  margin-left:15px;
  margin-top:15px;
  margin-bottom:15px;
}

.search-wrapper > ul {
  overflow-y:auto;  
  border-top: 1px solid #e7e7e7;
  border-bottom: 1px solid #e7e7e7;
  height:inherit;
}

.search-wrapper .modal-wrapper {
  margin:0;
}

.search-wrapper .document-list a{
  cursor: pointer;
}

.search-wrapper .pagination {
  display: table;
  margin: 15px auto;
}

.search-wrapper .overlay {
  background: #e9e9e9;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  opacity: 0.5;
  margin:0;
  text-align: center;
}

.overlay .fa-icon {
  height: 100%;
  width: 50%;
}

/* Filter modal */
.modal-backdrop{
  display:none;
}

.modal-dialog{
  margin: 60px auto;
}

.modal-custom-header{
  font-weight:bold;
  font-size:15px;
  color: #333;
}

.modal-dialog .checkbox-inline, .modal-dialog .radio-inline{
  margin:0px 15px;
}

.datepicker{
  padding-left:15px;
  padding-right:15px;
}

/* End of Filter modal */

#export-options .export-button{
  float:right;
}
</style>