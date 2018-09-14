<template>
    <div class="container">
        <div class="header">{{title}}</div>
        <slot></slot>
    </div>
</template>

<script>
export default {
  name: "CheckboxGroup",
  data() {
    return {
      selected: []
    };
  },
  props: {
    title: String
  },
  updated() {
    if (!this.$slots.default) return;
    this.$slots.default.forEach(checkbox => {
      checkbox.elm.removeEventListener("click", this.updated(checkbox));
      checkbox.selected = false;
      checkbox.elm.addEventListener("click", this.updated(checkbox), true);
    });
  },
  methods: {
    updated(checkbox) {
      return e => {
        var value = checkbox.data.attrs.value;
        if (!checkbox.elm.classList.contains("checked")) {
          if (this.selected.indexOf(value) == -1) this.selected.push(value);
        } else {
          if (this.selected.indexOf(value) > -1)
            this.selected.splice(this.selected.indexOf(value), 1);
        }
        this.$emit("changed");
        return true;
      };
    }
  }
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  width: 400px;
}

.header {
  background-color: #1a1a1a;
  color: white;
  font-size: 18px;
  padding: 10px;
  font-weight: bold;
  text-align: left;
  padding-left: 50px;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.9);
}
</style>
