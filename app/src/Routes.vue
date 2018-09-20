<script>
import VueRouter from "vue-router";
import App from "./App.vue";
import Timetable from "./components/Timetable.vue";

const routes = [
  { path: "/", component: App },
  { path: "/timetable", component: Timetable }
];

const router = new VueRouter({ routes });

export default routes;
</script>
