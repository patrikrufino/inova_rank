<template>
  <UContainer class="scroll-smooth">
    <h1 class="text-2xl font-bold my-5">
      Compartilhar uma nova ideia
    </h1>
    <div class="flex flex-col py-6">
      <label for="titulo" class="block font-semibold text-lg">
        Título
      </label>
      <input type="text" id="titulo"
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        placeholder="e.g. Aplicativo de ajuda a ONGs" required />
    </div>
    <div class="flex flex-col py-6">
      <label for="categoria" class="block font-semibold text-lg">
        Categoria
      </label>
      <select id="categoria"
        class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
        required>
        <option disabled value="">Selecione a categoria da sua ideia</option>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
    </div>

    <div class="flex flex-col py-6">
      <label for="descricao" class="block text-lg font-semibold">Desenvolvimento da ideia</label>
      <Editor v-model="info" />
      <div v-html="info"></div>
    </div>

    <div class="flex justify-end gap-6">
      <UButton color="red" variant="link" class="font-bold py-2 px-4 rounded">
        Cancelar
      </UButton>
      <UButton class="font-bold py-2 px-4 rounded">
        Publicar Ideia
      </UButton>
    </div>
  </UContainer>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { categoriesService } from '@/services/categoriesService';
import type { Category } from '@/services/categoriesService';

export default defineComponent({
  name: "New Idea",
  setup() {
    const categories = ref<Category[]>([]);
    const errorMessage = ref<string | null>(null);
    const info = ref<string>('');

    const fetchCategories = async () => {
      try {
        categories.value = await categoriesService.getAllCategories();
        console.log(categories.value)
        errorMessage.value = null;
      } catch (error) {
        console.error("Erro ao buscar categorias: ", error);
        errorMessage.value = "Ocorreu um problema ao buscar categorias. Tente novamente mais tarde.";
      }
    };

    onMounted(() => {
      fetchCategories();
    });

    return {
      categories,
      errorMessage,
      info,
    };
  },
});
</script>