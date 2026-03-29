import { apiClient } from "./client";

export const fetchFirstTester = async()=> {
    const response = await apiClient.get('/test-data');
    return response.data;
}