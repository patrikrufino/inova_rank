const BASE_URL = 'http://127.0.0.1:8000';

interface LoginResponse {
    access_token: string;
    refresh_token: string;
}

interface RegisterResponse {
    id: number;
    username: string;
    email: string;
}

interface AuthService {
    login(username: string, password: string): Promise<LoginResponse>;
    register(username: string, email: string, password: string): Promise<RegisterResponse>;
    refreshToken(refreshToken: string): Promise<LoginResponse>;
}

const authService: AuthService = {
    async login(username: string, password: string): Promise<LoginResponse> {
        const response = await fetch(`${BASE_URL}/auth/token`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (!response.ok) {
            throw new Error('Erro ao fazer login');
        }

        return response.json();
    },

    async register(username: string, email: string, password: string): Promise<RegisterResponse> {
        const response = await fetch(`${BASE_URL}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password }),
        });

        if (!response.ok) {
            throw new Error('Erro ao fazer cadastro');
        }

        return response.json();
    },

    async refreshToken(refreshToken: string): Promise<LoginResponse> {
        const response = await fetch(`${BASE_URL}/auth/refresh_token`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ refresh_token: refreshToken }),
        });

        if (!response.ok) {
            throw new Error('Erro ao renovar token');
        }

        return response.json();
    },
};

export default authService;