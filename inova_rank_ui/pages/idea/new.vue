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
      <label for="descricao" class="block text-lg font-semibold">Desenvolvimento da ideia</label>
      <textarea id="descricao" rows="4"
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" required></textarea>
    </div>

    <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded">
      Publicar Ideia
    </button>
  </UContainer>
</template>

<script setup>
</script>