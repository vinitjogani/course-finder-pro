<template>
    <div class="listing">

      <div class="search-container">
        <input type='text' v-model="query" value='' v-on:keyup="search"
          class="search-box" placeholder="Type to filter..." />
      </div>
      <span class="results-found">{{courses.length}} results found</span>

      <Course v-for="course in courses.slice(0, 100)"  :info="course"
        v-bind:key="course.id + course.course">
      </Course>

      <br><br>
    </div>
</template>

<script>
import Course from "./Course.vue";

export default {
  name: "Listing",
  props: ["courses"],
  components: { Course },
  data() {
    return {
      query: ""
    };
  },
  methods: {
    search() {
      this.$emit("search", this.query);
    }
  }
};
</script>

<style>
.search-container {
  display: flex;
  margin-bottom: 10px;
}

.search-box {
  padding: 15px;
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
  outline: none;
  border: none;
  border-radius: 2px;
  flex-grow: 1;
  margin-left: 20px;
  margin-right: 20px;
  transition: all 0.3s ease;
}

.search-box:focus {
  margin-left: 0px;
  margin-right: 0px;
  padding: 20px;
  transition: all 0.3s ease;
}

.results-found {
  color: rgba(0, 0, 0, 0.6);
  font-size: 12px;
  margin-bottom: 25px;
  display: block;
}

.listing {
  grid-column: 2;
  padding: 10px;
  text-align: center;
  overflow: auto;
  height: 100vh;
}
</style>

