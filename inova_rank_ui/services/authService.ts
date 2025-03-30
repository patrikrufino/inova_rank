const BASE_URL = "http://127.0.0.1:8000";

interface LoginResponse {
  access_token: string;
  token_type: string;
}

interface RegisterResponse {
  id: number;
  username: string;
  email: string;
}

interface AuthService {
  login(username: string, password: string): Promise<LoginResponse>;
  register(
    username: string,
    email: string,
    password: string
  ): Promise<RegisterResponse>;
  refreshToken(): Promise<LoginResponse>;
  isLoggedIn(): boolean;
  fetchWithAuth(url: string, options?: RequestInit): Promise<Response>;
  logout(): Promise<void>;
}

const authService: AuthService = {
  async login(username: string, password: string): Promise<LoginResponse> {
    try {
      const formdata = new URLSearchParams();
      formdata.append("username", username);
      formdata.append("password", password);

      const response = await fetch(`${BASE_URL}/auth/token`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formdata.toString(),
      });

      if (!response.ok) {
        if (response.status === 400) {
          throw new Error("Usuário ou senha incorretos");
        }
        throw new Error("Erro ao fazer login");
      }

      const data = await response.json();
      localStorage.setItem("access_token", data.access_token);
      return data;
    } catch (error) {
      console.error("Erro no login:", error);
      throw error;
    }
  },

  async register(
    username: string,
    email: string,
    password: string
  ): Promise<RegisterResponse> {
    try {
      const response = await fetch(`${BASE_URL}/users/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, email, password }),
      });

      if (!response.ok) {
        if (response.status === 409) {
          throw new Error("Nome de usuário ou email já cadastrado");
        }
        const errorData = await response.json();
        const errorMessage =
          errorData?.detail?.[0]?.msg || "Erro ao fazer cadastro";
        throw new Error(errorMessage);
      }

      return await response.json();
    } catch (error) {
      console.error("Erro no cadastro:", error);
      throw error;
    }
  },

  async refreshToken(): Promise<LoginResponse> {
    try {
      const response = await fetch(`${BASE_URL}/auth/refresh_token`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Erro ao renovar token");
      }

      const data = await response.json();
      localStorage.setItem("access_token", data.access_token);
      return data;
    } catch (error) {
      console.error("Erro ao renovar token:", error);
      throw error;
    }
  },

  isLoggedIn(): boolean {
    try {
      return !!localStorage.getItem("access_token");
    } catch (error) {
      console.error("Erro ao verificar login:", error);
      return false;
    }
  },

  async fetchWithAuth(
    url: string,
    options: RequestInit = {}
  ): Promise<Response> {
    try {
      const token = localStorage.getItem("access_token");
      if (token) {
        options.headers = {
          ...options.headers,
          Authorization: `Bearer ${token}`,
        };
      }
      return await fetch(url, options);
    } catch (error) {
      console.error("Erro ao fazer requisição autenticada:", error);
      throw error;
    }
  },

  async logout(): Promise<void> {
    try {
      localStorage.removeItem("access_token");
      console.log("Logout bem-sucedido");
    } catch (error) {
      console.error("Erro ao fazer logout:", error);
      throw error;
    }
  },
};

export default authService;
