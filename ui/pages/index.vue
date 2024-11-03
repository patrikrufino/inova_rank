<template>
  <UContainer class="scroll-smooth">
    <UCard
      v-for="idea in ideas"
      :key="idea.id"
      class="my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100"
    >
      <NuxtLink :to="`/idea/${idea.slug}`" class="block">
        <h1 class="text-xl font-semibold">
          {{ idea.name }}
        </h1>
        <div class="flex justify-end gap-6">
          <span>
            Criado {{ timeAgo(idea.created_at) }}
          </span>
          <span class="flex gap-2" title="Número de pessoas que acharam a ideia genial">
            <UIcon name="i-fluent-emoji-exploding-head" class="w-6 h-6" />
            {{ idea.num_genius }}
          </span>
          <span class="flex gap-2" title="Número de pessoas que acharam a ideia estúpida">
            <UIcon name="i-fluent-emoji-face-screaming-in-fear" class="w-6 h-6" />
            {{ idea.num_stupid }}
          </span>
        </div>
      </NuxtLink>
    </UCard>
  </UContainer>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';

interface Idea {
  id: number;
  name: string;
  slug: string;
  num_genius: number;
  num_stupid: number;
  created_at: string;
}

export default defineComponent({
  name: 'IdeasPage',
  setup() {
    const ideas = ref<Idea[]>([]);

    const fetchIdeas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/ideas/');
        const data = await response.json();
        ideas.value = data.items;
      } catch (error) {
        console.error('Error fetching ideas:', error);
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
      fetchIdeas();
    });

    return {
      ideas,
      timeAgo,
    };
  },
});
</script>