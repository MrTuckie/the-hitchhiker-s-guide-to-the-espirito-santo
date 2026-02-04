import axios from "axios"
console.log("aaaaaaaaaaa")
console.log(import.meta.env.VITE_API_URL);
const api = axios.create(
  { baseURL: import.meta.env.VITE_API_URL }
);

api.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default api
