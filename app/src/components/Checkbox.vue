<template>
    <div v-bind:class="'checkbox' + (checked ? ' checked': '')" v-on:click="toggleCheck">
        <div class="box">
            <span class="tick" v-if="checked"></span>
        </div>

        <span>{{ text }}</span>
    </div>
</template>

<script>
export default {
  name: "Checkbox",
  data() {
    return {
      checked: false
    };
  },
  props: {
    text: String
  },
  methods: {
    toggleCheck() {
      this.checked = !this.checked;
    }
  }
};
</script>


<style>
.checkbox {
  padding: 10px;
  box-sizing: border-box;
  background-color: rgb(50, 50, 50);
  color: #fff;
  display: flex;
  vertical-align: middle;
  min-height: 45px;
  cursor: pointer;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.9);
  /* white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; */
  text-align: left;
}

.checkbox.checked {
  background-color: #292929;
}

.checkbox .box {
  display: inline-block;
  height: 25px;
  min-width: 25px;
  background-color: #191919;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.9);
  margin-right: 15px;
}

.checkbox .box:hover {
  background-color: #000;
}

.checkbox span {
  padding: 4px;
}

.checkbox .box .tick {
  margin: 3px;
  width: 19px;
  height: 19px;
  box-sizing: border-box;
  display: inline-block;
  background-color: #b62a25;
}
</style>
