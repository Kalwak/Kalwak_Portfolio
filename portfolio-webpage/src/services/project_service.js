import axios from 'axios';

export class ProjectService {

    constructor() {
    }

    getProjects() {
        const url = '/api/project/';
        return axios.get(url).then(response => response.data);
    }

    getProject(pk) {
        const url = `/api/project/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
}