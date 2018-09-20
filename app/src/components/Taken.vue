<template>
    <div class="taken">
        <h1 class="eighty"  style="padding-left: 10px;">Hey there, help me help you!</h1>
        <p class="eighty" style="padding-left: 10px;">
            I am here to help you find courses you can actually take considering available seats, timetable conflicts, 
            and pre-requisite courses. Start by entering a list of comma-separated courses you've taken or will have
            taken by the time you plan to take the course you're looking for! Make sure to put the courses in the 
            specified format.<br><br>

            <b>Note:</b> This is not perfect in the sense that sometimes you may receive a course in your results
            that you can't actually take because of requirements like "need 5.0 FCE from this department's courses",
            or "permission of instructor". However, other than that, the tool matches the pre-reqs exactly and should
            be good enough in most cases. 
        </p>
        <textarea class="eighty" v-model="taken" placeholder="e.g. CSC148H1, CSC165H1"></textarea>

        <br><br>
        <button class="primary" v-on:click="next">NEXT</button>
    </div>
</template>

<script>
export default {
  name: "Taken",
  data() {
    return {
      taken: ""
    };
  },
  methods: {
    next() {
      this.$store.commit(
        "setTaken",
        this.taken
          .toUpperCase()
          .split(",")
          .map(x => x.trim())
          .filter(x => x != "")
      );
      this.$emit("next");
    }
  }
};
</script>

<style>
.taken {
  padding: 20px;
  text-align: left;
}

.taken textarea {
  height: 300px;
  border: none;
  outline: none;
  width: 80%;
  padding: 20px;
  font-family: "Roboto";
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
  resize: none;
}

h1 {
  color: black;
}
</style>

