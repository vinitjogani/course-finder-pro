<template>
    <div class="course" v-on:click="open">
          <b>{{info.course}}</b>: {{info.name}} ({{info.term}})<br>
          <em>Pre-requisites:</em> {{info.pre ? info.pre : 'None'}}<br>
          <em>Breadths:</em> {{info.breadths}}  
          

          <br><br>
          {{info.description}}
    </div>
</template>

<script>
var cfUrl =
  "http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId=";

export default {
  name: "Course",
  props: ["info"],
  methods: {
    open() {
      window.open(cfUrl + this.info.id);
    }
  }
};
</script>

<style>
.course {
  display: inline-block;
  width: 90%;
  padding: 20px;
  box-sizing: border-box;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);
  text-align: left;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.course:hover {
  box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
  transform: scale(1.03);
  transition: all 0.3s ease;
}
</style>
