import axios from '~/plugins/axios.js'

export default {
  getDocuments: function () {
    return axios.get('documents/')
  },

  hello: function () {
    alert('hello')
  }
}
