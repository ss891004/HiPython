<template>
  <div id="app">
    <div style="width:20%" class="container">
      <div>
        <h2>VUE + FastAPI</h2>
        <h3>演示前后端分离Hello World</h3>
        <h5>输入后端地址：</h5>
        <input type="text" class="form-control" v-model="address"/><br/>
        
        <h5>输入内容：</h5>
        <input type="text" class="form-control" v-model="hello"/><br/>
        <button type="button" class="btn btn-success" @click="registfn">发送到后端</button><br/><br/>
        
        <h5>FastAPI返回内容：</h5>
        {{fastapi_r}}<br/>
      </div>
    </div>
  </div>
</template>

<script>
  export default 
  {
    name: 'app',
    data() 
    {
      return {
        address:'http://192.168.101.69:8888/',
        hello:'HELLO',
        fastapi_r:''
      }
    },

    methods: 
    {
      registfn:function(){    //这是发送ajax的方法
        let _this = this
        this.axios({
          method:'get',
          url:this.address + this.hello, // get请求没有data:{}
        }).then(function(response)
          {     //这个then是发送完请求之后要执行的函数，回调函数
            console.log(response.data)
            // console.log(_this.fastapi_r)
            _this.fastapi_r = response.data
          });
      }
    },
  }
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
