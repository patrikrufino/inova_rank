// services/ideaService.ts
export interface Idea {
  id: number;
  title: string;
  slug: string;
  content: string;
  num_genius: number;
  num_stupid: number;
  created_at: string;
}

const API_URL = "http://127.0.0.1:8000/ideas/";

export class IdeaService {
  async getAllIdeas(): Promise<Idea[]> {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error("Erro ao buscar ideias");
      }
      const data = await response.json();
      return data.ideas;
    } catch (error) {
      console.error("Error fetching ideas:", error);
      throw error;
    }
  }

  async getIdeaBySlug(slug: string): Promise<Idea | null> {
    try {
      const response = await fetch(`${API_URL}${slug}`);
      if (!response.ok) {
        throw new Error("Erro ao buscar a ideia");
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error fetching idea:", error);
      throw error;
    }
  }

  async rateIdea(slug: string, type: "genius" | "stupid"): Promise<void> {
    try {
      const response = await fetch(`${API_URL}${slug}/rate?rate=${type}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: null,
      });
      if (!response.ok) {
        throw new Error("Erro ao registrar o voto");
      }
    } catch (error) {
      console.error("Error rating idea:", error);
      throw error;
    }
  }

  async unrateIdea(slug: string, type: "genius" | "stupid"): Promise<void> {
    try {
      const response = await fetch(`${API_URL}${slug}/unrate?rate=${type}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: null,
      });
      if (!response.ok) {
        throw new Error("Erro ao remover o voto");
      }
    } catch (error) {
      console.error("Error unrating idea:", error);
      throw error;
    }
  }
}

export const ideaService = new IdeaService();
