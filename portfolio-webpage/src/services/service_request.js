import axios from 'axios';
const API_URL = process.env.VUE_APP_API_ENDPOINT;


export class ServiceRequestService {

    constructor() {
    }

    postService(data) {
        const url = API_URL + '/api/service_request/';
        return axios.post(url, data).then(response => response.data);
    }
}