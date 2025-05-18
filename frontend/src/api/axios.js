import axios from 'axios';
const instance=axios.create({baseURL:process.env.REACT_APP_API_URL||'http://localhost:8000/api/'});
instance.interceptors.request.use(cfg=>{const t=localStorage.getItem('access');if(t)cfg.headers.Authorization=`Bearer ${t}`;return cfg;});
export default instance;