<template>
  <div>
    <UContainer class="scroll-smooth">
      <UNotification
        v-if="errorMessage"
        :description="errorMessage"
        :id="2"
        :timeout="5000"
        title="Erro"
        class="mt-5"
      />
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
            <span> Criado {{ timeAgo(idea.created_at) }} </span>
            <span
              v-for="(icon, index) in iconData"
              :key="index"
              class="flex gap-2"
              :title="icon.title"
            >
              <UIcon :name="icon.name" class="w-6 h-6" />
              {{ idea[icon.countKey as IdeaCountKey] }}
            </span>
          </div>
        </NuxtLink>
      </UCard>
    </UContainer>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { timeAgo } from "@/utils/timeUtils";
import { ideaService } from "@/services/ideaService";

interface Idea {
  id: number;
  name: string;
  slug: string;
  num_genius: number;
  num_stupid: number;
  created_at: string;
}

type IdeaCountKey = "num_genius" | "num_stupid";

export default defineComponent({
  name: "IdeasPage",
  setup() {
    const ideas = ref<Idea[]>([]);
    const errorMessage = ref<string | null>(null);
    const iconData = [
      {
        name: "i-fluent-emoji-exploding-head",
        countKey: "num_genius",
        title: "Número de pessoas que acharam a ideia genial",
      },
      {
        name: "i-fluent-emoji-face-screaming-in-fear",
        countKey: "num_stupid",
        title: "Número de pessoas que acharam a ideia estúpida",
      },
    ];

    const fetchIdeas = async () => {
      try {
        ideas.value = await ideaService.getAllIdeas();

        errorMessage.value = null;
      } catch (error) {
        console.error("Erro ao buscar ideias:", error);
        errorMessage.value =
          "Ocorreu um problema ao buscar as ideias. Tente novamente mais tarde.";
      }
    };

    onMounted(() => {
      fetchIdeas();
    });

    return {
      ideas,
      timeAgo,
      iconData,
      errorMessage,
    };
  },
});
</script>
