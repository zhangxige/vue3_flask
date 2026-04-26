import axios from 'axios'
import { showMessage } from './status' // 引入状态码文件
import { ElMessage } from 'element-plus' // 引入el 提示框，这个项目里用什么组件库这里引什么

// 设置接口超时时间
axios.defaults.timeout = 60000

// 请求地址，这里是动态赋值的的环境变量，下一篇会细讲，这里跳过
// axios.defaults.baseURL = import.meta.env.VITE_API_DOMAIN;
axios.defaults.baseURL = 'http://localhost:5000/' // 这里是本地测试地址，正式环境请使用上面那行代码
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*' // 注意：通常不应直接在客户端设置 Access-Control-Allow-Origin，这是服务器应该设置的头部。

//http request 拦截器
axios.interceptors.request.use(
  (config) => {
    // 配置请求头
    config.headers = config.headers || {}
    ;(config.headers as any)['Content-Type'] = 'application/json;charset=UTF-8' // 传参方式json
    ;(config.headers as any)['token'] = '80c483d59ca86ad0393cf8a98416e2a1' // 这里自定义配置，这里传的是token

    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

//http response 拦截器
axios.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    const { response } = error
    if (response) {
      // 请求已发出，但是不在2xx的范围
      showMessage(response.status) // 传入响应码，匹配响应码对应信息
      return Promise.reject(response.data)
    } else {
      ElMessage.warning('网络连接异常,请稍后再试!')
    }
  },
)

// 封装 GET POST 请求并导出
export function request(url = '', params = {}, type = 'POST') {
  //设置 url params type 的默认值
  return new Promise((resolve, reject) => {
    let promise: Promise<any> | undefined
    if (type.toUpperCase() === 'GET') {
      promise = axios({
        method: 'GET',
        url: url,
        data: params,
      })
    } else if (type.toUpperCase() === 'POST') {
      promise = axios({
        method: 'POST',
        url: url,
        data: params,
      })
    }
    //处理返回
    if (promise) {
      promise
        .then((res) => {
          console.log('请求成功', res)
          resolve(res)
        })
        .catch((err) => {
          reject(err)
        })
    } else {
      reject(new Error('Invalid request type'))
    }
  })
}
