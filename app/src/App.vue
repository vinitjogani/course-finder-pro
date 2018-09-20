<template>
  <div id="app">

    <Taken v-if="path == '/taken'"  v-on:next="path = '/timetable'" />

    <Timetable v-if="path == '/timetable'" v-on:next="path = '/results'" />

    <Results v-if="path == '/results'" />

    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">

  </div>
</template>

<script>
import Results from "./components/Results.vue";
import Timetable from "./components/Timetable.vue";
import Taken from "./components/Taken.vue";

import axios from "axios";

export default {
  name: "app",
  components: {
    Results,
    Timetable,
    Taken
  },
  data() {
    return {
      courses: [],
      filtered_courses: [],
      query: "",
      path: "/taken",
      timetable: [[], []]
    };
  },
  methods: {
    setTimetable() {
      this.path = "/results";
    }
  }
};
</script>

<style>
#app {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
}

body {
  margin: 0;
}

.loading {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: #191919;
  color: white;
  padding: 50px;
}

.eighty {
  margin-left: 10%;
  margin-right: 10%;
  box-sizing: border-box;
  width: 80%;
}

button.primary {
  background: white;
  padding: 10px;
  padding-left: 20px;
  padding-right: 20px;
  border: none;
  box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.2);
  font-family: "Roboto";
  font-weight: bold;
  cursor: pointer;
  font-size: 15px;
  float: right;
  margin-right: 10%;
}
</style>
