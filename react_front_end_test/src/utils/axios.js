import axios from "axios";




axios.interceptors.request.use(

)


axios.interceptors.response.use(
      response => {
            return response
      },
      error => {
            return Promise.reject(error)
      }
)


export default function request(url, opt) {
      const options = {}
      options.method = opt !== undefined ? opt.method : "get"
      if (opt) {
            if (opt.body) {
                  options.data = typeof opt.body === "string" ? JSON.parse(opt.body) : opt.body
            }

            if (opt.params !== undefined) {
                  url += '?'
                  for (let key in opt.params) {
                        if (opt.params[key] !== undefined && opt.params[key] !== '') {
                              url = url + key + '=' + opt.params[key] + '&'
                        }
                  }
                  url = url.substring(0, url.length - 1)
            }
      }
      return axios(
            { url, ...options, }
      ).then(
            response => {
                  return { ...response.data }
            }
      ).catch(error => {
            if (!error.response) {
                  return console.log("Error", error.message)
            }

            const status = error.response.status
            return { code: status }
      })

}