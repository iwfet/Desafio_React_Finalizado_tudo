import axios from 'axios';
const api = axios.create({
    baseURL: 'http://192.168.100.3:5000',
    timeout:1000
    
    //baseURL: 'https://api.tvmaze.com/search/shows?q='
})
export default api;