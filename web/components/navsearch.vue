<template>
	<div class="search-wrapper">
		<div class="sidebar-search">
	      <div class="sidebar-search-options">
	          <div class="has-feedback has-feedback-left search-option">
	              <input type="text" class="form-control" placeholder="Search..." />
	              <icon class="form-control-feedback" name="search"></icon>
	          </div>

	          <dropdown>
	              <button data-role="trigger" class="dropdown-toggle btn btn-default search-option icon-button" type="button">
	                  <icon name="filter"></icon>
	              </button>
	              <template slot="dropdown">
	                  <li>
	                      <div class="dropdown-header">
	                          Show only
	                      </div>
	                      <a v-for="filter in filters" @click.stop="toggleFilter(filter)">
	                          <div>
	                              <icon v-bind:style="{visibility: checkedFilters[filter] ? 'visible': 'hidden'}" name="check"></icon>
	                              <span>
	                                  {{ filter }}
	                              </span>
	                          </div>
	                      </a>

	                      <a>
	                          <div>
	                              <icon></icon>
	                              <span>
	                                  See more filters
	                              </span>
	                          </div>
	                      </a>
	                  </li>
	                  <li class="divider"></li>
	                  <li>
	                      <div class="dropdown-header">
	                          Sort by
	                      </div>
	                      <a @click.stop="setSortBy('newest')">
	                          <div>
	                              <icon v-bind:style="{visibility: sortBy == 'newest' ? 'visible': 'hidden'}" name="check"></icon>
	                              Date (newest)
	                          </div>
	                      </a>
	                      <a @click.stop="setSortBy('oldest')">
	                          <div>
	                              <icon v-bind:style="{visibility: sortBy == 'oldest' ? 'visible': 'hidden'}" name="check"></icon>
	                              Date (oldest)
	                          </div>
	                      </a>
	                      <a @click.stop="setSortBy('relevance')">
	                          <div>
	                              <icon v-bind:style="{visibility: sortBy == 'relevance' ? 'visible': 'hidden'}" name="check"></icon>
	                              Relevance
	                          </div>
	                      </a>
	                  </li>
	              </template>

	          </dropdown>

	          <div v-if="isDocActive == 'true'">
	              <button class=" btn btn-default search-option icon-button" type="button">
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
	  <ul class="nav" id="side-menu">
	      <li v-for="ao in aoDocuments" :key="ao.docNum">
	          <a href="/">
	              <div class="list-checkbox">
	                  <input v-bind:value="ao.docNum" type="checkbox" v-model="checkedAOs">
	              </div>
	              <div>
	                  <div>{{ ao.docNum }}</div>
	                  <div class="list-title text-muted"> 
	                      {{ ao.docTitle }}
	                  </div>
	              </div>
	          </a>
	      </li>
	 	</ul>
 	</div>
</template>

<script>
// icon imports
import 'vue-awesome/icons/search'
import 'vue-awesome/icons/filter'
import 'vue-awesome/icons/check'
import 'vue-awesome/icons/plus'
import 'vue-awesome/icons/download'

import dropdown from 'uiv/src/components/dropdown/Dropdown.vue'
import icon from 'vue-awesome/components/Icon'

export default {
  components: {
    dropdown,
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
      sortBy: 'newest'
    }
  },
  props: ['isDocActive'],
  methods: {
    selectAll: function (event) {
      for (let ao of this.aoDocuments) {
        this.checkedAOs.push(ao.docNum)
      }
    },
    deselectAll: function (event) {
      this.checkedAOs = []
    },
    downloadDocs: function (event) {
      this.deselectAll()
      alert('Document download')
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
  },
  mounted: function () {
    for (let filter of this.filters) { // initialize to check all filters
      this.$set(this.checkedFilters, filter, true)
    }
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

#export-options .export-button{
  float:right;
}
</style>