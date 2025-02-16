import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useCookie } from 'nuxt/app';
import axios from 'axios';
import { authAxios } from "@/composables/authAxiosSettings";

const newAxios = authAxios();

export const useAuthStore = defineStore('auth', () => {
    const accessToken = useCookie("accessToken");
    const refreshToken = useCookie("refreshToken");
    const isAuthenticated = ref(!!accessToken.value);
    const user = ref(null)
    const user_id = useCookie("id")
    const loadUser = ref(true)

    // onMounted(async () => {
    //     if (isAuthenticated.value === true && user.value === null) {
    //       isAuthenticated.value = true
    //         try {
    //             await fetchUser();
                
    //         } catch (error) {
    //             console.error("Error fetching user on mount:", error);
    //             isAuthenticated.value = false;
    //             user.value = null;
    //         } finally {
    //             loadUser.value = false;
    //         }
    //     }
    //     else {
    //       user.value = user.value
    //     }
    //   });

    async function login(access, refresh) {
        console.log(`В сторе в логине получили токены: ${access}, ${refresh}`)
        accessToken.value = access; // Устанавливаем куки
        refreshToken.value = refresh; // Устанавливаем куки
        isAuthenticated.value = !!accessToken.value;
        navigateTo('/')
        await fetchUser();                
    }

    function logout() {
        accessToken.value = null; // Удаляем куки
        refreshToken.value = null; // Удаляем куки
        accessToken.value = null;
        refreshToken.value = null;
        isAuthenticated.value = false;
        user_id.value = null
        user.value = null
    }

    async function fetchUser() {
      let res = null; // Создаем переменную для хранения результата
      
      try {
          const response = await newAxios.get('/profile-info/');
          if (response.data) {
              res = response.data; // Сохраняем данные в переменную
              console.log(`ПОЛУЧАЕМ ИНФОРМАЦИЮ ПО ЮЗЕРУ ${response.data}`)
          } else {
              console.warn("No user data found");
              console.log("No user data found");

          }
      } catch (error) {
          console.error("Error fetching user data:", error);
          console.log("Error fetching user data:", error);
          throw error; // Пробрасываем ошибку дальше
      } finally {
          // Здесь мы обновляем переменные только если res не null
          if (res) {
              console.log(res)
              user_id.value = res.id;
              user.value = res; // Обновляем данные пользователя
              loadUser.value = false
          } else {
            logout()
            navigateTo('/')
          }
      }
  }
    
  return {
    isAuthenticated,
    login,
    logout,
    accessToken,
    refreshToken,
    user,
    user_id,
    fetchUser,
    loadUser
  }
})