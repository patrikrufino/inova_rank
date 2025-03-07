<template>
    <UContainer class="scroll-smooth">
        <UCard class="my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">
            <h2 class="text-2xl font-bold mb-6 text-center">Cadastro</h2>
            <form @submit.prevent="register">
                <div class="mb-4">
                    <label class="block text-sm font-bold mb-2" for="name">Nome de usuário</label>
                    <input v-model="name" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Nom3Publ1c0" required>
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-bold mb-2" for="email">Email</label>
                    <input v-model="email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Digite seu email" required>
                </div>
                <div class="mb-6">
                    <label class="block text-sm font-bold mb-2" for="password">Senha</label>
                    <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Password" required>
                </div>
                <div class="flex items-center justify-between">
                    <UButton block class="bg-primary hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full" type="submit">
                        Cadastrar
                    </UButton>
                </div>
            </form>
        </UCard>
    </UContainer>
</template>

<script>
import authService from '@/services/authService';

export default {
    data() {
        return {
            name: '',
            email: '',
            password: ''
        };
    },
    methods: {
        async register() {
            try {
                const response = await authService.register(this.name, this.email, this.password);
                console.log('Registro bem-sucedido:', response);
                // Redirecionar ou mostrar uma mensagem de sucesso
            } catch (error) {
                console.error('Erro ao registrar:', error);
                // Mostrar uma mensagem de erro ao usuário
            }
        }
    }
};
</script>

<style scoped>
</style>