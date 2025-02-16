import axios from "axios";
import { useAuthStore } from "@/stores/auth";
import { useAuth } from "@/composables/auth"; // Импортируем useAuth
import { apiConfig } from "@/api/api";

export const authAxios = () => {
  const newAxios = axios.create({
    baseURL: apiConfig.API,
    headers: {
      "Content-Type": "application/json",
    },
  });

  // Добавляем интерсептор для установки токена
  newAxios.interceptors.request.use((config) => {
    const authStore = useAuthStore();
    const accessToken = authStore.accessToken;
    const refreshToken = authStore.refreshToken;

    if (accessToken && !config.url.includes("/registration") && !config.url.includes("/login") && !config.url.includes("/password-reset")) {
      config.headers.Authorization = `Bearer ${accessToken}`;
      config.headers.refresh_token = refreshToken; // refresh_token может не понадобиться в заголовках
    }

    return config;
  });

  // Интерсептор для обработки ошибок и рефреша токена
  newAxios.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      const originalRequest = error.config;
      const auth = useAuth(); // Получаем доступ к useAuth
      const authStore = useAuthStore(); // Получаем актуальный store

      // Проверяем, если ошибка 401 и запрос еще не повторен
      if (error.response?.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true; // Устанавливаем флаг, чтобы избежать бесконечного цикла
        
        try {
          // Обновляем токен
          const newAccessToken = await auth.fetchRefreshToken(); // Вызов функции обновления токена
          if (newAccessToken) {

            console.log(`Новый токен получен тут: ${newAccessToken}`)
            // Устанавливаем новый токен
            authStore.accessToken = newAccessToken; // Обновляем токен в store
            newAxios.defaults.headers.common.Authorization = `Bearer ${newAccessToken}`;
            return newAxios(originalRequest); // Повторяем оригинальный запрос
          }
        } catch (refreshError) {
          console.error("Ошибка обновления токена:", refreshError);
          //navigateTo("/"); // Перенаправляем на страницу логина
        }
      }

      // Если обновление токена не сработало или запрос уже был повторён
      if (error.response?.status === 401 && originalRequest._retry) {
        //navigateTo("/"); // Перенаправляем на страницу логина
      }

      return Promise.reject(error);
    }
  );

  return newAxios;
};