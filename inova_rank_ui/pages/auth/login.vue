<template>
    <UContainer class="scroll-smooth flex flex-col justify-center items-center min-h-screen">
        <img src="/login_hero.svg" alt="Homem sentado realizando login" class="w-48 mb-5"/>
        <UCard
            class="w-full md:max-w-1/2 my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">

            <template #header>
                <h1 class="text-2xl font-bold text-center">Login</h1>
            </template>
            <UForm :schema="schema" :state="state" @submit="onSubmit" class="space-y-4">
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
            </UForm>
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
import * as v from 'valibot';
import type { FormSubmitEvent } from '#ui/types';
import { UForm } from '#build/components';
import { reactive, ref } from 'vue';

export default {
    setup() {
        const schema = v.object({
            email: v.pipe(v.string(), v.email('Invalid email')),
            password: v.pipe(v.string(), v.minLength(8, 'Must be at least 8 characters'))
        });

        type Schema = v.InferOutput<typeof schema>;

        const state = reactive({
            email: '',
            password: ''
        });

        const passwordVisible = ref(false);

        const togglePasswordVisibility = () => {
            passwordVisible.value = !passwordVisible.value;
        };

        async function onSubmit(event: FormSubmitEvent<Schema>) {
            console.log(event.data);
        }

        return {
            schema,
            state,
            onSubmit,
            passwordVisible,
            togglePasswordVisibility
        };
    }
}
</script>