<script setup lang="ts">
import { ref, onMounted } from 'vue';

const isOpen = ref<boolean>(false);
const isDarkMode = ref<boolean>(false);

// Função para verificar a preferência de cor do usuário
const checkColorMode = () => {
  // Verifica se há uma preferência armazenada
  const storedPreference = localStorage.getItem('color-mode');
  if (storedPreference) {
    isDarkMode.value = storedPreference === 'dark';
  } else {
    // Se não houver preferência armazenada, verifica a configuração do sistema
    isDarkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
};

// Método para alternar entre os modos
const toggleColorMode = () => {
  isDarkMode.value = !isDarkMode.value;
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('color-mode', 'dark'); // Armazena a preferência
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('color-mode', 'light'); // Armazena a preferência
  }
};

// Verifica a preferência de cor ao montar o componente
onMounted(() => {
  checkColorMode();
  // Aplica a classe correta ao carregar
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
});
</script>

<template>
  <nav class="backdrop-blur-xl shadow-lg border-b dark:bg-gray-900/70 dark:border-gray-800 w-full top-0 sticky">
    <div class="mx-auto px-8 py-3 flex justify-between items-center">
      <NuxtLink to="/" class="text-xl font-bold">
        <img 
          :src="(isDarkMode ? '/inova_rank-logo-dark.svg' : '/inova_rank-logo-light.svg')" 
          alt="Inova Rank Logo" 
          class="h-5"
        />
      </NuxtLink>
      <div class="flex items-center space-x-3">
        <button @click="toggleColorMode" class="p-2">
          <span v-if="isDarkMode">
            <UIcon name="i-fluent-emoji-full-moon" class="w-6 h-6" />
          </span>
          <span v-else>
            <UIcon name="i-fluent-emoji-sun" class="w-6 h-6" />
          </span>
        </button>
        <NuxtLink to="/auth/login" class="font-semibold">Login</NuxtLink>
        <NuxtLink to="/auth/register" class="font-semibold">Cadastrar</NuxtLink>
      </div>    
    </div>
    <!-- mobile menu -->  
    <div :class="isOpen ? 'block' : 'hidden'" class="md:hidden">
      <!-- Aqui você pode adicionar o menu mobile se necessário -->
    </div>
  </nav>
</template>
