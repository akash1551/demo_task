<template>
  <div id="app">
    <div class="filter">
      <label for="">Search : </label>
      <input type="text" class="search-input" v-model="search_string" @input="searchSringData">
      <br>
      <label for="">Memory : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="Memory_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="Memory_end" @input="searchSringData">
      <label for="">vCPUs : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="vCPUs_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="vCPUs_end" @input="searchSringData">
      <!-- <label for="">Storage (GiB) : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="Storage_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="Storage_end" @input="searchSringData"> -->
      <br>
      <label for="">Linux On Demand Cost : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="Linux_demand_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="Linux_demand_end" @input="searchSringData">
      <label for="">Linux Reserved Cost : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="window_demand_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="Linux_reserved_end" @input="searchSringData">
      <label for="">Windows On Demand Cost : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="window_demand_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="window_demand_end" @input="searchSringData">
      <label for="">Windows Reserved Cost : </label>
      <input type="text" class="memory-input" placeholder="Start" v-model="window_reserved_start" @input="searchSringData">
      <input type="text" class="memory-input" placeholder="End" v-model="window_reserved_end" @input="searchSringData">
    </div>
    <div class="table_data" style="overflow-x:auto;">
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>API Name</th>
                    <th>Memory</th>
                    <th>vCPUs</th>
                    <th>Instance Storage</th>
                    <th>Network Performance</th>
                    <th>Linux On Demand Cost</th>
                    <th>Linux Reserved Cost</th>
                    <th>Windows On Demand Cost</th>
                    <th>Windows Reserved Cost</th>
                </tr>
            </thead>
            <tbody >
                <tr v-for="(item, index) in all_data_list" :key="index">
                    <td>{{item.name}}</td>
                    <td>{{item.api_name}}</td>
                    <td>{{item.memory}}</td>
                    <td>{{item.vcpu}}</td>
                    <td>{{item.instance_storage}}</td>
                    <td>{{item.network_performance}}</td>
                    <td>{{item.linux_on_demand_cost}}</td>
                    <td>{{item.linux_reserved_cost}}</td>
                    <td>{{item.windows_on_demand_cost}}</td>
                    <td>{{item.windows_reserved_cost}}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <!-- <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul> -->
  </div>
</template>

<script>
import { serverAddr } from "./network.config.js";

export default {
  name: 'app',
  data () {
    return {
      search_string : '',
      all_data_list: [],
      Memory_start: '',
      Memory_end: '',
      vCPUs_start: '',
      vCPUs_end: '',
      Storage_start: '',
      Storage_end: '',
      Linux_demand_start: '',
      Linux_demand_end: '',
      Linux_reserved_start: '',
      Linux_reserved_end: '',
      window_demand_start: '',
      window_demand_end: '',
      window_reserved_start: '',
      window_reserved_end: '',
    }
  },
  created() {
    serverAddr
      .post("filter/instance/", {

      })
      .then(this.getAllData)
      .catch(function(error) {
        console.log(error);
      });
    // this.axios.get(api).then((response) => {
    //   console.log(response.data)
    // })
  },
  methods:{
    searchSringData:function(){
      console.log('data',this.search_string);
      var memory_temp = {};
      memory_temp.start = this.Memory_start;
      memory_temp.end = this.Memory_end;
      var vcpu_temp = {};
      vcpu_temp.start = this.vCPUs_start;
      vcpu_temp.end = this.vCPUs_end;
      // var instance_storage_temp = {};
      // instance_storage.start = this.Storage_start;
      // instance_storage.end = this.Storage_end;
      var Linux_demand_temp = {};
      Linux_demand_temp.start = this.Linux_demand_start;
      Linux_demand_temp.end = this.Linux_demand_end;
      var Linux_reserved_temp = {};
      Linux_reserved_temp.start = this.Linux_reserved_start;
      Linux_reserved_temp.end = this.Linux_reserved_end;
      var window_demand_temp = {};
      window_demand_temp.start = this.window_demand_start;
      window_demand_temp.end = this.window_demand_end;
      var window_reserved_temp = {};
      window_reserved_temp.start = this.window_reserved_start;
      window_reserved_temp.end = this.window_reserved_end;
      console.log(memory_temp,'memory_temp');
     serverAddr
      .post("filter/instance/", {
        search_string : this.search_string,
        memory: memory_temp,
        vcpu: vcpu_temp,
        linux_on_demand_cost : Linux_demand_temp,
        linux_reserved_cost : Linux_reserved_temp,
        windows_on_demand_cost : window_demand_temp,
        windows_reserved_cost : window_reserved_temp,
      })
      .then(this.getAllData)
      .catch(function(error) {
        console.log(error);
      });
    },
    getAllData: function(response){
      if(response.data.status){
        this.all_data_list = [];
        this.all_data_list = response.data.data;
      }
    }

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}
#app .filter {
  margin-top: 20px;
}
#app .search-input {
  width: 200px;
  height: 30px;
  border-radius: 4px;
  border: 1px solid #ddd;
  margin-bottom: 10px;
}
#app .memory-input {
  width: 50px;
  height: 30px;
  padding-left: 5px;
  border-radius: 4px;
  border: 1px solid #ddd;
  margin: 10px 0;
}
.heading{
            width: 50%;
            margin-left: 25px;
        }
        .table_data {
            /* margin: 20px; */
            width: 100%;

        }

        table {
            border-collapse: collapse;
            width: 100%;
        }
        .input{
            width: 70%;
            height: 30px;
            border-radius: 4px;
            border: 1px solid #000;
            margin: 10px;
            padding-left: 10px;

        }

        /* tr:nth-child(even){background-color: #f2f2f2;} */

        /* tr:hover {background-color: #ddd;} */

        td {
            border: 1px solid #ddd;
            padding: 8px 8px;
            ;
            font-size: 15px;
        }

        th {
            padding-top: 12px;
            padding-left: 8px;
            padding-bottom: 12px;
            font-size: 15px;
            text-align: left;
            background-color: #5083CD;
            color: #f1f1f1;
            border: 1px solid #777;
        }

/* h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
} */
</style>
