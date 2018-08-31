import Vue from 'vue'
import axios from 'axios'
// import Toasted from 'vue-toasted'


// export const productionAddr = 'http://10.2.0.6:8000'
// export const productionAddr = 'http://192.168.1.108:8000'
// export const productionAddr = 'http://localhost:8000'
export const productionAddr = 'http://159.89.163.174:8888'

export const serverAddr = axios.create({
    baseURL: productionAddr,
    // baseURL: localAddr,
    timeout: 30000,

    headers: {},
    withCredentials: true,

transformRequest: [function (data, headers) {
    headers['Content-Type'] = "application/json;charset=UTF-8";
    // headers.common['Access-Control-Allow-Origin'] = "*";

    return JSON.stringify(data);
  }],
})
