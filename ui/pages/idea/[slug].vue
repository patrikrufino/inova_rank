<template>
  <UContainer class="mt-4">
    <UCard v-if="idea">
      <template #header>
        <span>{{ timeAgo(idea.created_at) }}</span>
        <h1 class="text-2xl font-bold">{{ idea.name }}</h1>
      </template>
      <p class="mt-4">{{ idea.content }}</p>
      <template #footer>
        <div class="flex justify-between gap-6 mt-4">
          <div class="w-full">
            <UButton 
            block
            icon="i-fluent-emoji-exploding-head"
            size="sm"
            color="primary"
            variant="soft"
            :label="`Genial ${idea.num_genius}`"
            :trailing="false"
            />
          </div>
          <div class="w-full">
            <UButton 
            block
            icon="i-fluent-emoji-face-screaming-in-fear"
            size="sm"
            color="primary"
            variant="soft"
            :label="`Estupida ${idea.num_stupid}`"
            :trailing="false"
            />
          </div>
        </div>
      </template>
    </UCard>
    <div v-else>
      <p>Carregando...</p>
    </div>
  </UContainer>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

interface Idea {
  id: number;
  name: string;
  slug: string;
  content: string;
  num_genius: number;
  num_stupid: number;
  created_at: string;
}

export default defineComponent({
  name: 'IdeaDetailPage',
  setup() {
    const route = useRoute();
    const idea = ref<Idea | null>(null);

    const fetchIdea = async () => {
      const slug = route.params.slug; // Obtém o slug da rota
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/ideas/${slug}`);
        if (!response.ok) {
          throw new Error('Erro ao buscar a ideia');
        }
        const data = await response.json();
        idea.value = data; // Supondo que a resposta contenha a ideia diretamente
      } catch (error) {
        console.error('Error fetching idea:', error);
      }
    };

    const timeAgo = (date: string): string => {
      const now = new Date();
      const seconds = Math.floor((now.getTime() - new Date(date).getTime()) / 1000);
      let interval = Math.floor(seconds / 31536000);

      if (interval > 1) return `${interval} anos atrás`;
      interval = Math.floor(seconds / 2592000);
      if (interval > 1) return `${interval} meses atrás`;
      interval = Math.floor(seconds / 86400);
      if (interval > 1) return `${interval} dias atrás`;
      interval = Math.floor(seconds / 3600);
      if (interval > 1) return `${interval} horas atrás`;
      interval = Math.floor(seconds / 60);
      if (interval > 1) return `${interval} minutos atrás`;
      return `${seconds} segundos atrás`;
    };

    onMounted(() => {
      fetchIdea();
    });

    return {
      idea,
      timeAgo,
    };
  },
});
</script>