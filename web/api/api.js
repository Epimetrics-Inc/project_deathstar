import axios from '~/plugins/axios.js'

export default {
  getDocuments: function (docquery) {
    var queryString = ''

    for (let key in docquery) {
      queryString += key + '=' + docquery[key] + '&'
    }
    return axios.get('documents/?' + queryString)
  },

  hello: function () {
    alert('hello')
  }
}
