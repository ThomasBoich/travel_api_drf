// ОСНОВНОЕ API
// const api_url = `http://localhost:8000/api`
// const api_url = `http://185.154.195.225/api`
export const base_url = 'http://127.0.0.1:8000'
const api_url = `${base_url}/api`

export const apiConfig = {
  API: api_url,
  users: `${api_url}/users/`,
  countries: `${api_url}/countries/`,
  cities: `${api_url}/cities/`,
  interests: `${api_url}/interests/`,
  totalTravelCount: `${api_url}/totalTravelCount/`,
  travelCount: `${api_url}/countries/total_country_count/`,
  travels: `${api_url}/travels/`,
  trips: `${api_url}/trips/`,
  trips_filter: `${api_url}/trips/filter`,
  travel: `${api_url}/travels/filter/info`,
  travels_list: `${api_url}/travels/list/`,
  travels_filter: `${api_url}/travels/filter`,
  countries_from_moscow: `${api_url}/travels/countries_from_moscow/`,
  travel_from_moscow_now: `${api_url}/from_moscow/`
}
// export const API = 'http://127.0.0.1:8000/api/'
export const API = `${api_url}`