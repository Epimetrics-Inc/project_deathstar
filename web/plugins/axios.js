import axios from 'axios'

export default axios.create({
  baseURL: 'http://35.198.220.54/api/',
  timeout: 10000,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})
