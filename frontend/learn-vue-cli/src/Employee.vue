<template>
  <div>
   <h3>{{Message}}</h3><br><br>
   <form @submit.prevent="addArticle()" method="post">
   <input type="text" placeholder="Enter heading" v-model="article.heading"><br><br>
   <input type="text" placeholder="Ener body" v-model="article.body"><br><br>
   <button type="submit">submit</button>
   </form>
   
  </div>
</template>

<script>

export default {
  
  data () {
    return {
      Message : 'Welcome to Employee Component',
      article:
      {
        heading:"",
        body:""
      },
      
      
    }
  },
 

  methods:
  {
      addArticle()
      {
         var data={
         heading:"this is heading",
        body:"this is description"
        }
        console.log(data);
        this.$http.post("http://localhost:8000/api/addarticle/",data
          ).then(function(response)
        
        {
         console.log(response);
        });
      }
  },
  created()
  {
    this.$http.get("http://localhost:8000/api/show/").then(function(data)
    {

      console.log(data);
    });
  }
 
}
</script>

<style scoped>
h3{
  color:red;
}
</style>
