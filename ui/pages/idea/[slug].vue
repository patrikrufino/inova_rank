<template>
  <UContainer class="mt-4">
    <UNotification
      v-if="errorMessage"
      :description="errorMessage"
      :id="2"
      :timeout="5000"
      title="Erro"
    />
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
              :disabled="currentVote === 'genius'"
              @click="toggleVote('genius')"
            />
          </div>
          <div class="w-full">
            <UButton 
              block
              icon="i-fluent-emoji-face-screaming-in-fear"
              size="sm"
              color="primary"
              variant="soft"
              :label="`Estúpida ${idea.num_stupid}`"
              :trailing="false"
              :disabled="currentVote === 'stupid'"
              @click="toggleVote('stupid')"
            />
          </div>
        </div>
      </template>
    </UCard>
  </UContainer>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { timeAgo } from '@/utils/timeUtils';
import { ideaService } from '@/services/ideaService';

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
    const errorMessage = ref<string | null>(null);
    const currentVote = ref<'genius' | 'stupid' | null>(null);

    const fetchIdea = async () => {
      const slug = route.params.slug as string;
      try {
        idea.value = await ideaService.getIdeaBySlug(slug);
        if (!idea.value) {
          throw new Error('Ideia não encontrada');
        }
        errorMessage.value = null; 
      } catch (error) {
        console.error('Error fetching idea:', error);
        errorMessage.value = 'Ocorreu um problema ao buscar a ideia. Tente novamente mais tarde.';
      }
    };

    const toggleVote = async (type: 'genius' | 'stupid') => {
      const slug = route.params.slug as string;
      try {
        if (currentVote.value === type) {
          // Se já votou na mesma opção, desmarcar
          await ideaService.unrateIdea(slug, type);
          currentVote.value = null;
        } else {
          // Se votou em uma opção diferente, mudar o voto
          if (currentVote.value) {
            await ideaService.unrateIdea(slug, currentVote.value);
          }
          // Votar na nova opção
          await ideaService.rateIdea(slug, type);
          currentVote.value = type;
        }
      } catch (error) {
        console.error('Error toggling vote:', error);
        errorMessage.value = 'Ocorreu um problema ao registrar seu voto. Tente novamente mais tarde.';
      }
    };

    onMounted(() => {
      fetchIdea();
    });

    return {
      idea,
      timeAgo,
      errorMessage,
      currentVote,
      toggleVote,
    };
  },
});
</script>
