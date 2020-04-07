<template>
  <div>
   <employee></employee>
  </div>
</template>

<script>
import Employee from './Employee.vue'
import Student from './Student.vue'
export default {
components:
{
  "employee":Employee,
  "student":Student
}
  ,
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      info:'this is simple data',
      control:"student"
      
    }
  },
  methods:
  { 
 
}
}
</script>

<style>

</style>
