<template>
    <div class="flex justify-center items-center min-h-screen">
      <UContainer class="welcome-page flex flex-col md:flex-row justify-center items-center">
          <img src="/welcome_hero.svg" alt="Ilustração de uma pessoa tendo uma ideia inovadora" class="md:max-w-96 md:mr-8 mb-4 md:mb-0" />
          <UCard class="md:max-w-1/2">
            <template #header>
              <h1 class="text-2xl font-bold text-primary">Bem-vindo à Inova Rank, {{ userName }}!</h1>
            </template>
            <p class="text-lg">
              E aí, beleza? Você acaba de entrar para a comunidade Inova Rank, um espaço feito para quem pensa fora da
              caixa e quer transformar o mundo com ideias incríveis. Aqui, a inovação não tem limites e a colaboração é a chave
              para o sucesso. Bora inovar juntos?
            </p>
            <UButton variant="soft" class="mt-4 w-full" block to="/dashboard">Começar a Inovar</UButton>
          </UCard>
      </UContainer>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'WelcomePage',
    setup() {
      const userName = ref('Inovador');
      return {
        userName,
      };
    },
  });
  </script>