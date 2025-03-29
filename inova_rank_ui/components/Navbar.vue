<script setup lang="ts">
import { ref, onMounted } from 'vue';
import authService from '@/services/authService';
import { useRouter } from 'vue-router';
import { useAuth } from '@/composables/useAuth';
import { _backgroundColor } from '#tailwind-config/theme';

const isOpen = ref<boolean>(false);
const isDarkMode = ref<boolean>(false);
const router = useRouter();
const { isLoggedIn, checkAuth } = useAuth();

const themeTabs = [
  { label: 'Light', icon: 'i-heroicons-sun-16-solid' },
  { label: 'Dark', icon: 'i-heroicons-moon-solid' },
];
const menuItems = [
  [{
    label: 'Perfil',
    icon: 'i-heroicons-user-circle-20-solid',
  }], [{
    label: 'Adicionar nova ideia',
    icon: 'i-heroicons-plus-circle-20-solid',
    click: () => {
      router.push('/idea/new');
    }
  }, {
    label: 'Minhas ideias',
    icon: 'i-heroicons-queue-list'
  },
  {
    label: 'Editar perfil',
    icon: 'i-heroicons-cog-6-tooth-solid'
  },], [{
    label: 'color-mode',
    slot: 'color-mode',

  }], [{
    label: 'Deslogar',
    icon: 'i-heroicons-arrow-left-end-on-rectangle-16-solid',
    slot: 'logout',
    click: () => {
      handleLogout();
    }
  }]
]

const checkColorMode = () => {
  const storedPreference = localStorage.getItem('color-mode');
  if (storedPreference) {
    isDarkMode.value = storedPreference === 'dark';
  } else {
    isDarkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
};

const toggleColorMode = () => {
  isDarkMode.value = !isDarkMode.value;
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('color-mode', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('color-mode', 'light');
  }
};

const handleLogout = async () => {
  try {
    await authService.logout();
    await checkAuth();
    router.push('/auth/login');
  } catch (error) {
    console.error('Erro ao fazer logout:', error);
  }
};

onMounted(async () => {
  checkColorMode();
  await checkAuth();
});
</script>

<template>
  <nav class="backdrop-blur-xl shadow-lg border-b dark:bg-gray-900/70 dark:border-gray-800 w-full top-0 sticky">
    <div class="mx-auto px-8 py-3 flex justify-between items-center">
      <NuxtLink to="/" class="text-xl font-bold">
        <img :src="(isDarkMode ? '/inova_rank-logo-dark.svg' : '/inova_rank-logo-light.svg')" alt="Inova Rank Logo"
          class="h-5" />
      </NuxtLink>
      <div class="flex items-center space-x-3">
        <button v-show="!isLoggedIn" @click="toggleColorMode" class="p-2">
          <span v-if="isDarkMode">
            <UIcon name="i-heroicons-moon-solid" class="w-6 h-6" />
          </span>
          <span v-else>
            <UIcon name="i-heroicons-sun-16-solid" class="w-6 h-6" />
          </span>
        </button>
        <NuxtLink v-show="!isLoggedIn" to="/auth/login" class="font-semibold">Login</NuxtLink>
        <NuxtLink v-show="!isLoggedIn" to="/auth/register" class="font-semibold">Cadastrar</NuxtLink>
        <UTooltip v-show="isLoggedIn" text="Adicionar nova ideia" placement="bottom">
          <NuxtLink to="/idea/new">
            <UButton icon="i-heroicons-plus-16-solid" size="sm" square variant="ghost" color="black" />
          </NuxtLink>
        </UTooltip>
        <UTooltip v-show="isLoggedIn" text="Menu" placement="bottom">
          <UDropdown v-show="isLoggedIn" :items="menuItems" :popper="{ placement: 'bottom-start' }">
            <UButton color="white" trailing-icon="i-mdi-menu" />
            <template #logout="{ item }">
              <UIcon :name="item.icon" class="h-6 w-6 text-red-500" />
              <span class="text-red-500 font-bold">
                {{ item.label }}
              </span>
            </template>
            <template #color-mode="{ item }" :ui>
              <UIcon :name="item.icon" />
              <UTabs :items="themeTabs" :default-index="!isDarkMode ? 0 : 1" @change="toggleColorMode">
                <template #icon="{ item, selected }">
                  <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0 me-2"
                    :class="[selected && 'text-primary dark:text-primary']" />
                </template>
              </UTabs>
            </template>
          </UDropdown>
        </UTooltip>

      </div>
    </div>
    <!-- mobile menu -->
    <div :class="isOpen ? 'block' : 'hidden'" class="md:hidden">
    </div>
  </nav>
</template>