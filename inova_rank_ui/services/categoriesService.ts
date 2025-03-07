export interface Category {
    id: number;
    name: string;
}

const API_URL = "http://127.0.0.1:8000/categories/";

export class CategoriesService {
    async getAllCategories(): Promise<Category[]> {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) {
                throw new Error("Erro ao buscar categorias");
            }
            const data = await response.json();
            return data.categories;
        } catch (error) {
            console.error("Error fetching categories:", error);
            throw error;
        }
    }
}

export const categoriesService = new CategoriesService();