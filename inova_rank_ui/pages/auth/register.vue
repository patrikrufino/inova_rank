<template>
    <UContainer class="scroll-smooth">
            <UCard class="my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">
                <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
                <form @submit.prevent="login">
                    <div class="mb-4">
                        <label class="block text-sm font-bold mb-2" for="email">Email</label>
                        <input v-model="email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Digite seu email" required>
                    </div>
                    <div class="mb-6">
                        <label class="block text-sm font-bold mb-2" for="password">Senha</label>
                        <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="Digite sua senha" placeholder="Password" required>
                    </div>
                    <div class="flex items-center justify-between">
                        <button class="bg-primary hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full" type="submit">
                            Login
                        </button>
                    </div>
                </form>
                <div class="text-center flex justify-center items-center mt-4">
                    <p class="mr-2 text-sm">Novo no InovaRank?</p>
                    <NuxtLink to="/auth/register" class="text-sm font-semibold text-primary hover:text-emerald-600 underline">Crie sua conta aqui.</NuxtLink>
                </div>
                <div class="text-center flex justify-center items-center mt-4">
                    <p class="mr-2 text-sm">Esqueceu sua senha?</p>
                    <NuxtLink to="/auth/forgot-password" class="underline font-semibold text-sm text-primary hover:text-emerald-600">Clique aqui.</NuxtLink>
                </div>
            </Ucard>
    </UContainer>

</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        register() {
            // Handle registration logic here
            console.log('Registering:', this.name, this.email, this.password);
        }
    }
};
</script>

<style scoped>
</style>