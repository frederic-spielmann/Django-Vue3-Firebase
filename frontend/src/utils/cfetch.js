import { useUsersStore } from '@/stores/users.store'

const backendEndpoint = `${import.meta.env.VITE_BACKEND_URL}`

export const cfetch = {
    get: request('GET'),
    post: request('POST'),
    put: request('PUT'),
    delete: request('DELETE')
}

export function request(method) {
    return async (endpoint, body) => {
        const userStore = useUsersStore()
        const user = await userStore.currentUser()
        const tokenId = await user.getIdToken()
        const url = `${backendEndpoint}${endpoint}`
        const options = {
            method: method
        }
        if (tokenId) {
            options["headers"] = {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${tokenId}`
            }
        }
        if (body) {
            options.body = JSON.stringify(body);
        }

        return fetch(url, options)
        .then(response=> {
            const isJson = response.headers?.get('content-type')?.includes('application/json')
            const data = isJson ? response.json() : null
            if (!response.ok) {
                const error = (data && data.message) || response.status
                return Promise.reject(error)
            }
            return data
        })
    }
}