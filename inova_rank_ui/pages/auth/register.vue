<template>
    <UContainer class="scroll-smooth flex flex-col justify-center items-center min-h-screen">
        <img src="/sign_up_hero.svg" alt="Homem sentado realizando login" class="w-48 mb-5" />
        <UCard
            class="w-full md:max-w-1/2 my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">
            <h2 class="text-2xl font-bold mb-6 text-center">Cadastro</h2>
            <form @submit.prevent="onSubmit" class="space-y-4">
                <UFormGroup label="Nome de usuário" name="name">
                    <UInput v-model="name" placeholder="Nom3Publ1c0" size="lg" required />
                </UFormGroup>
                <UFormGroup label="Email" name="email">
                    <UInput v-model="email" placeholder="Digite seu email" size="lg" required />
                </UFormGroup>
                <UFormGroup label="Senha" name="password">
                    <div class="relative">
                        <UInput :type="passwordVisible ? 'text' : 'password'" v-model="password" placeholder="Digite sua senha" size="lg" required />
                        <button type="button" @click="togglePasswordVisibility('password')"
                            :class="passwordVisible ? 'text-primary' : ''"
                            class="absolute inset-y-0 right-0 pr-3 flex items-center">
                            <UIcon :name="passwordVisible ? 'i-mdi-eye' : 'i-mdi-eye-off'" class="w-6 h-6" />
                        </button>
                    </div>
                </UFormGroup>
                <UFormGroup label="Confirmar senha" name="confirmPassword">
                    <div class="relative mb-2" >
                        <UInput :type="confirmPasswordVisible ? 'text' : 'password'" v-model="confirmPassword" placeholder="Confirme sua senha" size="lg" required />
                        <button type="button" @click="togglePasswordVisibility('confirmPassword')"
                            :class="confirmPasswordVisible ? 'text-primary' : ''"
                            class="absolute inset-y-0 right-0 pr-3 flex items-center">
                            <UIcon :name="confirmPasswordVisible ? 'i-mdi-eye' : 'i-mdi-eye-off'" class="w-6 h-6" />
                        </button>
                    </div>
                    <UAlert v-if="passwordMismatch" title="As senhas não coincidem" variant="subtle" color="red"/>
                </UFormGroup>
                <transition name="fade">
                    <UAlert v-show="showError" :title="'Erro ao realizar cadastro'" :description="errorMessage" color="red"
                        variant="subtle" />
                </transition>
                <div class="flex items-center justify-between">
                    <UButton block
                        class="bg-primary hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
                        type="submit">
                        Cadastrar
                    </UButton>
                </div>
            </form>
        </UCard>
    </UContainer>
</template>

<script lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import authService from '@/services/authService';

export default {
    setup() {
        const router = useRouter();
        const name = ref('');
        const email = ref('');
        const password = ref('');
        const confirmPassword = ref('');
        const passwordVisible = ref(false);
        const confirmPasswordVisible = ref(false);
        const showError = ref(false);
        const errorMessage = ref('');

        // Computed property para verificar se as senhas coincidem
        const passwordMismatch = computed(() => password.value !== confirmPassword.value && confirmPassword.value !== '');

        // Alterna a visibilidade dos campos de senha
        const togglePasswordVisibility = (field: 'password' | 'confirmPassword') => {
            if (field === 'password') {
                passwordVisible.value = !passwordVisible.value;
            } else if (field === 'confirmPassword') {
                confirmPasswordVisible.value = !confirmPasswordVisible.value;
            }
        };

        // Valida e envia o formulário
        const onSubmit = async () => {
            // Valida se as senhas coincidem antes de enviar
            if (passwordMismatch.value) {
                showError.value = true;
                errorMessage.value = 'As senhas não coincidem.';
                return;
            }

            try {
                // Envia os dados para o serviço de autenticação
                const response = await authService.register(name.value, email.value, password.value);
                console.log('Registro bem-sucedido:', response);

                // Redireciona para a página de boas-vindas
                router.push('/welcome');
            } catch (error) {
                console.error('Erro ao registrar:', error);
                showError.value = true;
                errorMessage.value = 'Erro ao registrar. Tente novamente.';
            }
        };

        return {
            name,
            email,
            password,
            confirmPassword,
            passwordVisible,
            confirmPasswordVisible,
            showError,
            errorMessage,
            passwordMismatch,
            togglePasswordVisibility,
            onSubmit,
        };
    },
};
</script>