import axios from 'axios';

export class ProjectService {

    constructor() {
    }

    getProjects() {
        const url = API_URL + `/api/project/`;
        return axios.get(url).then(response => response.data);
    }

    getProject(pk) {
        const url = API_URL + `/api/project/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
}