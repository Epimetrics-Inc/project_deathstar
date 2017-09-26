import axios from '~/plugins/axios.js'

export default {
  getDocuments: function (docquery) {
    var queryString = ''

    for (let key in docquery) {
      queryString += key + '=' + docquery[key] + '&'
    }
    return axios.get('documents/?' + queryString)
  },

  getDocument: function (docPK) {
    return axios.get('documents/' + docPK + '/')
  }
}
