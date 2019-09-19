import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        projectsInformation: [],
        // organized information, with I'll work with the
        // projects pagination
        projects: {
            projectsCategory: '',
            projects: [],
            currentProject: {},
            currentProjectId: 0,
        },
        userIp: '',
    },

    mutations: {
        // mutations to set values for projects, which is an object where
        // data like which project is shown now (matched with a view)
        // like the current category and current project id
        setCategory: (state, category) => state.projects.projectsCategory = category,
        // setProjectId: (state, id) => state.projects.projectId = id,
        setProjects: (state, projects) => state.projects.projects = projects,
        setCurrentProject: (state, project) => state.projects.currentProject = project,
        setAllProjects: (state, projects) => state.projectsInformation = projects,
        setUserIp: (state, ip) => state.userIp = ip,
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
                    console.log(errors);
                });
        },
    },

    getters: {
        numberOfProjects(state) {
            return state.projects.projects.length;
        },
    },
});
