<template>
	<div class="VueToNuxtLogo">

	    <nav class="navbar navbar-default navbar-static-top" role="navigation">
	        <div class="navbar-header">                     
	            <button type="button" class="navbar-toggle" v-on:click="toogleSideBar">
	                    <span class="sr-only">Toggle navigation</span>
	                    <span class="icon-bar"></span>
	                    <span class="icon-bar"></span>
	                    <span class="icon-bar"></span>
	                </button>


	            <nuxt-link class="navbar-brand" to="/">Omnibus</nuxt-link>
	        </div>
	        <!-- /.navbar-header -->

	        <ul class="nav navbar-top-links navbar-right ">
	            <li v-bind:class="{ active: isDocActive }">
	                <nuxt-link to="/">Documents</nuxt-link>
	            </li>
	            <li v-bind:class="{ active: isVisActive }">
	                <nuxt-link to="visualization">Visualization</nuxt-link>
	            </li>
	            <li v-bind:class="{ active: isAboutActive }">
	                <nuxt-link to="about">About</nuxt-link>
	            </li>               
	        </ul>
	        <!-- /.navbar-top-links -->
	    </nav>
    </div>
</template>

<script>
export default {
  props: ['isVisActive', 'isDocActive', 'isAboutActive'],
  methods: {
    toogleSideBar: function (event) {
      this.$emit('tooglesidebar')
    }
  }
}
</script>