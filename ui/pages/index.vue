<template>
    <UContainer class="scroll-smooth">
      <UCard v-for="idea in ideas" :key="idea.id" class="my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100">
          <h1 class="text-xl font-semibold">
            {{ idea.name }}
          </h1>
          <div class="flex justify-end gap-4">
            <span class="flex gap-2" >
              <UIcon name="i-fluent-emoji-exploding-head" class="w-6 h-6"/> 
              {{ idea.num_genius }}
            </span>
            <span class="flex gap-2">
              <UIcon name="i-fluent-emoji-face-screaming-in-fear" class="w-6 h-6"/> 
              {{ idea.num_stupid }}
            </span>
          </div>
      </UCard>
    </UContainer>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'IdeasPage',
  setup() {
    const ideas = ref<any[]>([]);

    const fetchIdeas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/ideas/');
        const data = await response.json();
        ideas.value = data.items;
      } catch (error) {
        console.error('Error fetching ideas:', error);
      }
    };

    onMounted(() => {
      fetchIdeas();
    });

    return {
      ideas,
    };
  },
});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.ideas-list {
  list-style-type: none;
  padding: 0;
}

.idea-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
  width: 300px;
  text-align: center;
}
</style>
