<template>
    <div class="sidebar">
        <h1 style="color: white; display:inline-block;">Filter courses</h1>
        
        <button class="primary" style="margin-top:25px" 
          v-on:click="$store.commit('navigate', '/timetable')">
          BACK
        </button>

        <CheckboxGroup v-on:changed="updateBreadths" ref="breadths" title="Breadths">
            <Checkbox text="BR1: Creative and Cultural Expression" :value="1" />
            <Checkbox text="BR2: Thoughts, Beliefs and Behaviour" :value="2" />
            <Checkbox text="BR3: Society and its Institutions" :value="3" />
            <Checkbox text="BR4: Living Things and their Environment" :value="4" />
            <Checkbox text="BR5: Physical and Mathematical Universe" :value="5" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateCampus" ref="campus" title="Campus">
            <Checkbox text="St. George" :value="'UTSG'" />
            <Checkbox text="Scarborough" :value="'UTSC'" />
            <Checkbox text="Mississauga" :value="'UTM'" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateCredits" ref="credits" title="Credits">
            <Checkbox text="Half-year course" :value="0.5" />
            <Checkbox text="Full-year course" :value="1.0" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateTerms" ref="terms" title="Terms">
            <Checkbox text="2018 Fall" :value="'2018 Fall'" />
            <Checkbox text="2019 Winter" :value="'2019 Winter'" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateLevels" ref="levels" title="Levels">
            <Checkbox text="100-level" :value="100" />
            <Checkbox text="200-level" :value="200" />
            <Checkbox text="300-level" :value="300" />
            <Checkbox text="400-level" :value="400" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateMedium" ref="medium" title="Medium">
            <Checkbox text="Online-only" :value="1" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateDuplicates" ref="duplicates" title="Duplicates">
            <Checkbox text="One section per course" :value="1" />
        </CheckboxGroup>

        <CheckboxGroup v-on:changed="updateDepartments" ref="departments" title="Departments">
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
  methods: {
    updateBreadths() {
      this.$store.commit("setBreadths", this.$refs.breadths.selected);
    },
    updateCampus() {
      this.$store.commit("setCampus", this.$refs.campus.selected);
    },
    updateTerms() {
      this.$store.commit("setTerms", this.$refs.terms.selected);
    },
    updateCredits() {
      this.$store.commit("setCredits", this.$refs.credits.selected);
    },
    updateLevels() {
      this.$store.commit("setLevels", this.$refs.levels.selected);
    },
    updateDepartments() {
      this.$store.commit("setDepartments", this.$refs.departments.selected);
    },
    updateMedium() {
      this.$store.commit("setMedium", this.$refs.medium.selected);
    },
    updateDuplicates() {
      this.$store.commit("setDuplicates", this.$refs.duplicates.selected);
    }
  },
  updated() {
    console.log("Props updated");
    if (
      this.$store.state.request.departments.filter(
        e => this.departments.indexOf(e) < 0
      ).length
    ) {
      this.$store.commit(
        "setDepartments",
        this.$store.state.request.departments.filter(
          e => this.departments.indexOf(e) > -1
        )
      );
    }
  }
};
</script>

<style>
h1 {
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