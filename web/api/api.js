import axios from '~/plugins/axios.js'

export function getDocuments (docquery) {
  var queryString = ''

  for (let key in docquery) {
    queryString += key + '=' + docquery[key] + '&'
  }
  return axios.get('documents/?' + queryString)
}

export function getDocument (docPK) {
  return axios.get('documents/' + docPK + '/')
}
