import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        projectsInformation: [],
        projects: {
            projectsCategory: '',
            projects: [],
            currentProject: {},
            currentProjectId: 0,
        },
        userIp: '',
        onSearching: false,
        searchText: '',
        filter: {
            year: '',
            month: '',
        },
    },

    mutations: {
        setCategory: (state, category) => state.projects.projectsCategory = category,
        setProjects: (state, projects) => state.projects.projects = projects,
        setCurrentProject: (state, project) => state.projects.currentProject = project,
        setAllProjects: (state, projects) => state.projectsInformation = projects,
        setUserIp: (state, ip) => state.userIp = ip,
        setOnSearching: (state, status) => state.onSearching = status, 
        setSearchText: (state, text) => state.searchText = text,
        setYear: (state, year) => state.filter.year = year,
        setMonth: (state, month) => state.filter.month = month
    },

    actions: {
        setProjectsByCategory({commit, state}) {
            let category = state.projects.projectsCategory;
            let categorizedProjects = [];
            let projects = state.projectsInformation;

            // going through every project object
            // and check if the current page category matches with theirs
            projects.forEach(project => {
                if (project.categories.indexOf(category) > -1) {
                    project.pageId = categorizedProjects.length + 1;
                    categorizedProjects.push(project);
                }
            });

            if (categorizedProjects) {
                // setting projects.projects to the categorized projects
                commit('setProjects', categorizedProjects);
                // set emptyMatch to false to say that we have not empty matches
            }
            // after projects has been set, now will
        },
        getUserIp({ commit }) {
            let endpoint = `${process.env.VUE_APP_API_ENDPOINT}/api/get-ip/`;
            axios.get(endpoint)
                .then( response => {
                    let  ip = response.data.ip;
                    commit('setUserIp', ip);
                })
                .catch( errors => {
                    console.error(errors);
                });
        },
    },

    getters: {
        numberOfProjects(state) {
            return state.projects.projects.length;
        },
    },
});
