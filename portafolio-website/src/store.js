import Vue from 'vue';
import Vuex from 'vuex';
import config from '../config/config';
import axios from 'axios';
Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    envVariables: config,
    team: {
      members: []
    }
  },
  mutations: {
    /**
      * @function setTeamMembers
      * @param Object state 
      * @param Array teamMembers [Array of objects containing information of a member]
      * @return void
    */
    setTeamMembers(state, teamMembers) {
      state.team.members = teamMembers;
    }
  },
  actions: {
    async getTeamMembersData({ commit, state }) {
      let data = localStorage.getItem('teamMembersData');
      if (!data) {
        const resp = await axios.get(state.envVariables.teamMembersEndpoint);
        commit('setTeamMembers', resp.data);
        localStorage.setItem('teamMembersData', JSON.stringify(resp.data));
      } else commit('setTeamMembers', JSON.parse(data));;
    }
  }
});