import { useState } from "#app";
import authService from "@/services/authService";

export const useAuth = () => {
  const isLoggedIn = useState<boolean>("isLoggedIn", () => false);

  const checkAuth = async () => {
    try {
      isLoggedIn.value = await authService.isLoggedIn();
    } catch (error) {
      console.error("Erro ao verificar autenticação:", error);
      isLoggedIn.value = false;
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
      isLoggedIn.value = false;
    } catch (error) {
      console.error("Erro ao fazer logout:", error);
    }
  };

  return {
    isLoggedIn,
    checkAuth,
    logout,
  };
};
