import axios from 'axios';

export class ServiceRequestService {

    constructor() {
    }

    postService(data) {
        const url = '/api/service_request/';
        return axios.post(url, data).then(response => response.data);
    }
}
