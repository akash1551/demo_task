<template>
  <div id="app">
    <div class="filter">
      <label for="">Search : </label>
      <input type="text" class="search-input" v-model="search_string" @input="searchSringData">
    </div>
     <div style="display: flex;">
        <div class="heading">
            <h3>Movies filmed in San Francisco City</h3>
        </div>
        <div class="heading">
            <!-- <input type="text" class="input" id="myInput" onkeyup="myFunction()" placeholder="Search Title"> -->
        </div>
    </div>
    <!-- <p>{{data}}</p> -->
    <div class="table_data">
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
                    <th>Windows On Demand Cost</th>
                </tr>
            </thead>
            <tbody >
                <tr v-for="(item, index) in items" :key="index">
                    <td>{{item.title}}</td>
                    <td>{{item.release_year}}</td>
                    <td>{{item.location}}</td>
                    <td>{{item.fun_fact}}</td>
                    <td>{{item.production_company}}</td>
                    <td>{{item.distributor}}</td>
                    <td>{{item.director}}</td>
                    <td>{{item.writer}}</td>
                    <td>{{item.actor1}}</td>
                    <td>{{item.actor2}}</td>
                    <td>{{item.actor3}}</td>
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
     serverAddr
      .post("filter/instance/", {
        search_string : this.search_string
      })
      .then(this.getAllData)
      .catch(function(error) {
        console.log(error);
      });
    },
    getAllData: function(response){
      all_data_list = response.data.data;
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
#app .search-input {
  width: 200px;
  height: 30px;
  border-radius: 4px;
  border: 1px solid #ddd;
}
.heading{
            width: 50%;
            margin-left: 25px;
        }
        .table_data {
            margin: 20px;
            width: 100%
        }

        table {
            border-collapse: collapse;
            width: 100%;
            overflow-x: scroll;
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
            text-align: left;
            background-color: #eee;
            color: #333;
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
