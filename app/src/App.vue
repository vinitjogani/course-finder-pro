<template>
  <div id="app" style="overflow-y: hidden;">

    <transition name="fade">
      <Taken style="height: 100vh; box-sizing: border-box;" 
        v-if="$store.state.path == '/taken'"  />
    </transition>

    <transition name="fade">
      <Timetable v-if="$store.state.path == '/timetable'" />
    </transition>

    <transition name="fade">
      <Results v-if="$store.state.path == '/results'" />
    </transition>

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
      timetable: [[], []]
    };
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
  max-height: 100vh;
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

.fade-enter-active {
  transition-property: all;
  transition-duration: 0.5s;
  transition-delay: 0.5s;
}

.fade-leave-active {
  transition-property: all;
  transition-duration: 0.5s;
}

.fade-enter {
  margin-top: 100vh;
}

.fade-leave-to {
  opacity: 0;
}
</style>
