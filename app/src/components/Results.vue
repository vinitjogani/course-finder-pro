<template>
    <div class="results">
        <!-- v-on:changed="update" -->

     <FilterBar ref="filter" :terms="terms"
        :departments="departments" />

      <Listing v-on:search="search" 
        :courses="filtered(filtered_courses)" />

        <div class="loading">
            Loading...
        </div>
    </div>
</template>

<script>
import FilterBar from "./FilterBar.vue";
import Listing from "./Listing.vue";
import axios from "axios";

export default {
  name: "Results",
  components: { FilterBar, Listing },
  data() {
    return {
      courses: [],
      query: "",
      path: "/timetable",
      timetable: [[], []]
    };
  },
  computed: {
    filtered_courses() {
      var request = this.$store.state.request;
      var output = [];
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
          (!request.medium.length ||
            course.times[course.times.length - 1][0] == "ONLINE") &&
          (!request.duplicates.length || shown.indexOf(course.id) == -1)
        ) {
          output.push(course);
          shown.push(course.id);
        }
      }

      return output;
    },
    departments() {
      var output = [];
      for (var course of this.filtered_courses) {
        if (output.indexOf(course["department"]) < 0)
          output.push(course["department"]);
      }
      return output.sort();
    }
  },
  methods: {
    valid(searched, found) {
      return !searched.length || searched.indexOf(found) + 1;
    },
    refresh() {
      var req = JSON.stringify(this.$store.state.request);
      axios
        .post("http://localhost:5000/get-courses", { request: req })
        .then(data => {
          this.courses = data.data;
          console.log(data);
          document.getElementsByClassName("loading")[0].style.display = "none";
        });
    },
    search(query) {
      this.query = query;
    },
    filtered(courses) {
      return courses.filter(
        course =>
          (course.course.indexOf(this.query.toUpperCase()) + 1 ||
            course.name.toLowerCase().indexOf(this.query.toLowerCase()) + 1) &&
          this.valid(this.$store.state.request.departments, course.department)
      );
    }
  },
  mounted() {
    this.refresh();
  }
};
</script>

<style>
.results {
  display: grid;
  grid-template-columns: 450px 1fr;
}
</style>
