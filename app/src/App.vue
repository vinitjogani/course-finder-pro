<template>
  <div id="app">
    <FilterBar v-on:changed="update" ref="filter" :departments="unique('department')" />
    <Listing v-on:search="search" :courses="filtered_courses" />
    
    <div class="loading">
      Loading...
    </div>
  </div>
</template>

<script>
import FilterBar from "./components/FilterBar.vue";
import Listing from "./components/Listing.vue";
import axios from "axios";

export default {
  name: "app",
  components: {
    FilterBar,
    Listing
  },
  data() {
    return {
      courses: [],
      filtered_courses: [],
      query: ""
    };
  },
  methods: {
    update(request) {
      this.filtered_courses = [];
      var shown = [];

      for (var course of this.courses) {
        var breadths_intersection = request.breadths.filter(
          e => course.breadths.indexOf(e) > -1
        );

        if (
          this.valid(request.terms, course.term) &&
          this.valid(request.campus, course.campus) &&
          this.valid(request.levels, course.level) &&
          this.valid(request.credits, course.credits) &&
          (breadths_intersection.length || !request.breadths.length) &&
          this.filtered(course) &&
          (!request.medium.length ||
            course.times[course.times.length - 1][0] == "ONLINE") &&
          (!request.duplicates.length || shown.indexOf(course.id) == -1) &&
          this.valid(request.departments, course.department)
        ) {
          this.filtered_courses.push(course);
          shown.push(course.id);
        }
      }
    },
    valid(searched, found) {
      return !searched.length || searched.indexOf(found) + 1;
    },
    refresh() {
      var req = JSON.stringify(this.$refs.filter.request);
      axios
        .post("http://localhost:5000/get-courses", { request: req })
        .then(data => {
          this.courses = data.data;
          this.update(this.$refs.filter.request);
          document.getElementsByClassName("loading")[0].style.display = "none";
        });
    },
    unique(field) {
      var output = [];
      for (var course of this.courses) {
        if (output.indexOf(course[field]) < 0) output.push(course[field]);
      }
      return output.sort();
    },
    search(query) {
      this.query = query;
      this.update(this.$refs.filter.request);
    },
    filtered(course) {
      return (
        course.course.indexOf(this.query.toUpperCase()) + 1 ||
        course.name.toLowerCase().indexOf(this.query.toLowerCase()) + 1
      );
    }
  },
  mounted() {
    this.refresh();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: grid;
  grid-template-columns: 450px 1fr;
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
</style>
