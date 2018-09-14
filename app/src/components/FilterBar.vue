<template>
    <div class="sidebar">
        <h1>Filter courses</h1>

        <CheckboxGroup v-on:changed="update" ref="breadths" title="Breadths">
            <Checkbox text="BR1: Creative and Cultural Expression" :value="1" />
            <Checkbox text="BR2: Thoughts, Beliefs and Behaviour" :value="2" />
            <Checkbox text="BR3: Society and its Institutions" :value="3" />
            <Checkbox text="BR4: Living Things and their Environment" :value="4" />
            <Checkbox text="BR5: Physical and Mathematical Universe" :value="5" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="campus" title="Campus">
            <Checkbox text="St. George" :value="'UTSG'" />
            <Checkbox text="Scarborough" :value="'UTSC'" />
            <Checkbox text="Mississauga" :value="'UTM'" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="credits" title="Credits">
            <Checkbox text="Half-year course" :value="0.5" />
            <Checkbox text="Full-year course" :value="1.0" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="terms" title="Terms">
            <Checkbox text="2018 Fall" :value="'2018 Fall'" />
            <Checkbox text="2019 Winter" :value="'2019 Winter'" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="levels" title="Levels">
            <Checkbox text="100-level" :value="100" />
            <Checkbox text="200-level" :value="200" />
            <Checkbox text="300-level" :value="300" />
            <Checkbox text="400-level" :value="400" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="medium" title="Medium">
            <Checkbox text="Online-only" :value="1" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="duplicates" title="Duplicates">
            <Checkbox text="One section per course" :value="1" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="update" ref="departments" title="Departments">
            <Checkbox v-for="department in departments" v-bind:key="department"
                :text="department" :value="department"  />
        </CheckboxGroup>

        <br><br>
    </div>
</template>


<script>
import Checkbox from "./Checkbox.vue";
import CheckboxGroup from "./CheckboxGroup.vue";

export default {
  name: "FilterBar",
  components: {
    Checkbox,
    CheckboxGroup
  },
  props: ["departments"],
  data() {
    return {
      request: {
        breadths: [],
        campus: [],
        terms: [],
        credits: [],
        timetable: [],
        taken: [
          "CSC148H1",
          "PHY132H1",
          "MAT135H1",
          "MAT136H1",
          "ECO101H1",
          "ECO102H1",
          "COG250Y1",
          "CSC165H1",
          "CSC207H1",
          "MAT223H1",
          "APM236H1",
          "CSC236H1"
        ],
        departments: [],
        levels: [],
        medium: [],
        duplicates: []
      }
    };
  },
  methods: {
    update() {
      this.filtered_courses = [];

      this.request.breadths = this.$refs.breadths.selected;
      this.request.campus = this.$refs.campus.selected;
      this.request.terms = this.$refs.terms.selected;
      this.request.credits = this.$refs.credits.selected;
      this.request.levels = this.$refs.levels.selected;
      this.request.departments = this.$refs.departments.selected;
      this.request.medium = this.$refs.medium.selected;
      this.request.duplicates = this.$refs.duplicates.selected;

      this.$emit("changed", this.request);
    }
  }
};
</script>

<style>
h1 {
  color: white;
  text-align: left;
  font-weight: bolder;
  padding-left: 10px;
}

.sidebar {
  grid-column: 1;
  background-color: #191919;
  padding: 4px;
  position: fixed;
  height: 100%;
  overflow: auto;
}
</style>