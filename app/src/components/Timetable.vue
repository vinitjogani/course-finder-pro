<template>
  <div>
    <h1 class="eighty">Perfect! Let's move on...</h1>
    <p class="eighty" style="text-align: left; padding-left: 10px;">
      Proceed by filling in your timetable by clicking and dragging over the times you won't be available. Note 
      that if you are only looking for a courses in a particular semester, you may choose to not fill the other
      semester's timetable.
    </p>
    <div class="hbox eighty" style="height: calc(100vh - 250px);">
        <div class="vbox" v-for="(tt, term) in ['Fall', 'Winter']" :key='tt'>
            <!-- <div class="tools">
                <div class="left" v-if="term == 0">
                    Add your timetable
                </div>
                <div class="right" v-if="term == 1">
                   <button v-on:click="timetable[0].splice(0); timetable[1].splice(0);">
                       Clear
                    </button>
                   <button v-on:click="next">Next</button>
                </div>
            </div> -->
            <div class="heading">{{tt}}</div>
            <div class="hbox timetable">
                <div class="day hours">
                    <div class="heading">Time</div>
                    <div class="hour" v-for="hour in hours" :key="hour">
                        <div class="spacer"></div>
                        <span>{{ hour < 10 ? '0' + hour : hour }}:00</span>
                        <div class="spacer"></div>
                    </div>
                </div>
                <div class="day" v-for="day in days" :key="day">
                    <div class="heading">
                        {{day}}
                    </div>
                    <div :class="'time' + ((time % 1) ? '': ' hour') + colored(term, day.toUpperCase(), time + 0.5)" 
                        v-for="time in times" :key="day + time"
                        v-on:click="toggle(term, day.toUpperCase(), time + 0.5)"
                        v-on:mousemove="e => turnon(term, day.toUpperCase(), time + 0.5)(e)"
                        v-on:mousedown="mousestart(term, day.toUpperCase(), time + 0.5)">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br><br>
    <button class="primary" v-on:click="next">NEXT</button>
  </div>
</template>

<script>
export default {
  name: "Timetable",
  data() {
    return {
      tab: "Fall",
      days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      times: [],
      hours: [],
      timetable: [
        [
          // Fall
        ],
        [
          // Winter
        ]
      ],
      on: false
    };
  },
  methods: {
    toggle(term, day, time) {
      this.turnon(term, day, time)({ buttons: 1 });
    },
    turnon(term, day, time) {
      var slot = JSON.stringify([day, time, time + 0.5]);
      return e => {
        if (!e.buttons) return true;
        if (this.timetable[term].indexOf(slot) < 0 && this.on) {
          this.timetable[term].push(slot);
        } else if (!this.on && this.timetable[term].indexOf(slot) >= 0) {
          this.timetable[term].splice(this.timetable[term].indexOf(slot), 1);
        }
        return true;
      };
    },
    mousestart(term, day, time) {
      var slot = JSON.stringify([day, time, time + 0.5]);
      this.on = this.timetable[term].indexOf(slot) < 0;
    },
    colored(term, day, time) {
      var slot = JSON.stringify([day, time, time + 0.5]);
      return this.timetable[term].indexOf(slot) + 1 ? " black" : "";
    },
    next() {
      this.$store.commit("setTimetable", this.timetable);
      this.$emit("next");
    }
  },
  mounted() {
    for (var i = 8.5; i < 22.5; i += 0.5) {
      this.times.push(i);
      if (!(i % 1)) this.hours.push(i);
    }
  }
};
</script>

<style>
body {
  margin: 0;
  font-family: "Roboto", sans-serif;
}

.fullscreen {
  max-width: 100vw !important;
  max-height: 100vh !important;
  min-height: 100vh !important;
}

.timetable {
  flex-grow: 1;
}

.day {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  text-align: center;
  box-shadow: 0 0 3px rgba(0, 0, 0, 0.1);
}

.time,
.hour {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  user-select: none;
  text-align: center;
}

.time {
  border-bottom: solid;
  border-color: rgba(0, 0, 0, 0.05);
  cursor: pointer;
}

.hour {
  border-bottom: solid;
  border-color: rgba(0, 0, 0, 0.1);
}

.hours .hour {
  background-color: rgb(250, 250, 250);
}

.spacer {
  flex-grow: 1;
}

.heading {
  text-align: center;
  background-color: rgb(240, 240, 240);
  padding: 10px;
  user-select: none;
}

.hbox,
.vbox {
  display: flex;
  flex-grow: 1;
}

.vbox {
  flex-direction: column;
}

.hbox {
  flex-direction: row;
}

.black {
  background-color: #292929;
}

.tools {
  height: 60px;
  padding: 15px;
  font-size: 20px;
  box-sizing: border-box;
  background-color: #191919;
}

.left {
  text-align: left;
  font-weight: bolder;
}

.right {
  text-align: right;
}

.left,
.right {
  color: #b62a25;
}

.tools button {
  background: #b62a25;
  outline: none;
  border: none;
  padding: 10px;
  font-weight: bolder;
  margin-top: -5px;
  cursor: pointer;
  margin-right: 10px;
}
</style>