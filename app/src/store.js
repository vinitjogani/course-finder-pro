import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        request: {
            breadths: [],
            campus: [],
            terms: [],
            credits: [],
            timetable: [[/* Fall */], [/* Winter */]],
            taken: [],
            departments: [],
            levels: [],
            medium: [],
            duplicates: []
        }
    },
    mutations: {
        setBreadths(state, breadths) {
            state.request.breadths = breadths;
        },
        setCampus(state, campus) {
            state.request.campus = campus;
        },
        setTerms(state, terms) {
            state.request.terms = terms;
        },
        setCredits(state, credits) {
            state.request.credits = credits;
        },
        setTimetable(state, timetable) {
            state.request.timetable = timetable;
        },
        setTaken(state, taken) {
            state.request.taken = taken;
        },
        setDepartments(state, departments) {
            state.request.departments = departments;
        },
        setLevels(state, levels) {
            state.request.levels = levels;
        },
        setMedium(state, medium) {
            state.request.medium = medium;
        },
        setDuplicates(state, duplicates) {
            state.request.duplicates = duplicates;
        },
        updateFilter(state, request) {
            state.request.breadths = request.breadths;
            state.request.terms = request.terms;
            state.request.credits = request.credits;
            state.request.levels = request.levels;
            state.request.medium = request.medium;
            state.request.duplicates = request.duplicates;
            state.request.campus = request.campus;
        }
    }
})

export default store;