<template>
    <UContainer class="scroll-smooth flex flex-col justify-center items-center min-h-screen">
        <img src="/login_hero.svg" alt="Homem sentado realizando login" class="w-48 mb-5" />
        <UCard
            class="w-full md:max-w-1/2 my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">

            <template #header>
                <h1 class="text-2xl font-bold text-center">Login</h1>
            </template>
            <form @submit.prevent="onSubmit" class="space-y-4">
                <UFormGroup label="Email" name="email">
                    <UInput v-model="state.email" placeholder="Digite seu email" size="lg" />
                </UFormGroup>
                <UFormGroup label="Senha" name="password">
                    <div class="relative">
                        <UInput :type="passwordVisible ? 'text' : 'password'" v-model="state.password"
                            placeholder="Digite sua senha" size="lg" />
                        <button type="button" @click="togglePasswordVisibility"
                            :class="passwordVisible ? 'text-primary' : ''"
                            class="absolute inset-y-0 right-0 pr-3 flex items-center">
                            <UIcon :name="passwordVisible ? 'i-mdi-eye' : 'i-mdi-eye-off'" class="w-6 h-6" />
                        </button>
                    </div>
                </UFormGroup>
                <transition name="fade">
                    <UAlert v-show="showError" :title="'Erro ao realizar login'" :description="errorMessage" color="red"
                        variant="subtle" />
                </transition>
                <UButton block
                    class="bg-primary hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
                    type="submit">
                    Login
                </UButton>
                <div class="text-center flex justify-center items-center mt-4">
                    <p class="mr-2 text-sm">Novo no InovaRank?</p>
                    <NuxtLink to="/auth/register"
                        class="text-sm font-semibold text-primary hover:text-emerald-600 underline">Crie
                        sua conta aqui.</NuxtLink>
                </div>
            </form>
            <div class="text-center flex justify-center items-center mt-4">
                <p class="mr-2 text-sm">Esqueceu sua senha?</p>
                <NuxtLink to="/auth/forgot-password"
                    class="underline font-semibold text-sm text-primary hover:text-emerald-600">
                    Clique aqui.</NuxtLink>
            </div>
        </UCard>
    </UContainer>
</template>

<script lang="ts">
import { reactive, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import authService from '@/services/authService';

export default {
    setup() {
        const router = useRouter();
        const state = reactive({
            email: '',
            password: ''
        });

        const passwordVisible = ref(false);
        const showError = ref(false);
        const errorMessage = ref('');
        const isLoggedIn = ref(false);
        const redirectCountdown = ref(5);

        const togglePasswordVisibility = () => {
            passwordVisible.value = !passwordVisible.value;
        };

        async function onSubmit() {
            console.log('Form submitted', state);
            try {
                await authService.login(state.email, state.password);
                router.go(0);
            } catch (error) {
                console.error(error);
                showError.value = true;
                setTimeout(() => {
                    showError.value = false;
                }, 5000);
                errorMessage.value = (error as any).message || 'Erro desconhecido';
            }
        }

        onMounted(async () => {
            if (await authService.isLoggedIn()) {
                isLoggedIn.value = true;
                router.push('/');
            }
        });

        return {
            state,
            onSubmit,
            passwordVisible,
            togglePasswordVisibility,
            showError,
            errorMessage,
            isLoggedIn,
            redirectCountdown,
        };
    }
}
</script>