//@ts-ignore
import { useAuthStore } from "../stores/auth";
import { authAxios } from "@/composables/authAxiosSettings";
import { useCookie } from 'nuxt/app';
export function useAuth () {
  // Инициализация стора и токенов
  const authStore = useAuthStore();

  const newAxios = authAxios()

  // Функция регистрации
  async function login(email, password){
    try {
      const response = await newAxios.post('/login/', {
        email,
        password
      });

      if (response.data) {
        const access = response.data.access_token;
        const refresh = response.data.refresh_token;
        authStore.login(access, refresh);
        console.log(`Мы получили токены в логин функции: ${access}, ${refresh}`);
        
      };

    } catch (error){
      console.error("Ошибка при входе:", error);
    }
  }
  

  async function logout(){
    authStore.logout()
    navigateTo("/");
  }


  async function fetchRefreshToken() {
    const refresh = useCookie('refreshToken');
    try {
      console.log(` КЛЮЧ ИЗ КУКОВ ТУТ ${refresh.value}`)

      const response = await newAxios.post(
        `/token/refresh/`,
        {
          refresh: refresh.value, // Отправляем refresh токен
        },
      );
      
      if (response.data) {
        const newAccess = response.data.access; // Новый access токен
        const newRefresh = response.data.refresh; // Новый access токен
        // Сохранение токенов в куки
        useCookie('accessToken').value = newAccess;
        // useCookie('refreshToken').value = newRefresh;
        console.log(`новые токены: ${newAccess} и ${newRefresh}`);
        return newAccess;
      }
    } catch (error) {
      console.log(refresh.value)
      console.error("Ошибка при обновлении токена:", error);
      authStore.logout()
    }
  }
  


  // Следим За Обновлением Состояния Пользователя
  // watch(
  //   () => authStore.isAuthenticated,
  //   (newValue) => {
  //     isAuthenticated.value = newValue;
  //   },
  // );

  // watch(
  //   () => authStore.user,
  //   (newValue) => {
  //     user.value = newValue;
  //   },
  // );

  return {
    login,
    logout,
    fetchRefreshToken,
  }
}