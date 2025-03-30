<template>
    <UContainer class="scroll-smooth flex flex-col justify-center items-center min-h-screen">
        <img src="/sign_up_hero.svg" alt="Homem encostado em um celular com a tela de registro" class="w-48 mb-5" />
        <UCard
            class="w-full md:max-w-1/2 my-5 hover:cursor-pointer hover:shadow-lg hover:shadow-primary/30 transition-shadow duration-1000 delay-100 max-w-lg mx-auto">
            <h2 class="text-2xl font-bold mb-6 text-center">Cadastro</h2>
            <form @submit.prevent="onSubmit" class="space-y-4">
                <UFormGroup label="Nome de usuário" name="name">
                    <UInput v-model="name" placeholder="Nom3Publ1c0" size="lg" required />
                    <transition enter-active-class="duration-500 ease-in opacity-0" enter-to-class="opacity-100"
                        leave-active-class="duration-500 ease-out" leave-class="opacity-100" leave-to-class="opacity-0">
                        <div v-if="name.length > 0" class="mt-2">
                            <UProgress :color="nameColor" :value="nameScore" :max="3" size="sm" />
                            <p class="text-sm font-medium mt-2">{{ nameText }}</p>
                            <ul class="space-y-1">
                                <li v-for="(req, index) in nameStrength" :key="index"
                                    :class="req.met ? 'text-green-500' : 'text-red-500'">
                                    <UIcon :name="req.met ? 'i-mdi-check-circle' : 'i-mdi-close-circle'"
                                        class="w-4 h-4" />
                                    <span class="ml-2">{{ req.text }}</span>
                                </li>
                            </ul>
                        </div>
                    </transition>
                </UFormGroup>
                <UFormGroup label="Email" name="email">
                    <UInput v-model="email" placeholder="Digite seu email" size="lg" required />
                    <transition enter-active-class="duration-500 ease-in opacity-0" enter-to-class="opacity-100"
                        leave-active-class="duration-500 ease-out" leave-class="opacity-100" leave-to-class="opacity-0">
                        <p v-if="!emailValid" class="text-red-500 text-sm mt-1 font-semibold">
                            Email inválido
                        </p>
                    </transition>
                </UFormGroup>
                <UFormGroup label="Senha" name="password">
                    <div class="relative">
                        <UInput :color="color" :type="passwordVisible ? 'text' : 'password'" v-model="password"
                            placeholder="Digite sua senha" size="lg" required />
                        <button type="button" @click="togglePasswordVisibility('password')"
                            :class="passwordVisible ? 'text-primary' : ''"
                            class="absolute inset-y-0 right-0 pr-3 flex items-center">
                            <UIcon :name="passwordVisible ? 'i-mdi-eye' : 'i-mdi-eye-off'" class="w-6 h-6" />
                        </button>
                    </div>
                    <transition enter-active-class="duration-500 ease-in opacity-0" enter-to-class="opacity-100"
                        leave-active-class="duration-500 ease-out" leave-class="opacity-100" leave-to-class="opacity-0">
                        <div v-if="password.length > 0" class="mt-2">
                            <UProgress :color="color" :value="score" :max="4" size="sm" />
                            <p class="text-sm font-medium mt-2">{{ text }}</p>
                            <ul class="space-y-1">
                                <li v-for="(req, index) in strength" :key="index"
                                    :class="req.met ? 'text-green-500' : 'text-red-500'">
                                    <UIcon :name="req.met ? 'i-mdi-check-circle' : 'i-mdi-close-circle'"
                                        class="w-4 h-4" />
                                    <span class="ml-2">{{ req.text }}</span>
                                </li>
                            </ul>
                        </div>
                    </transition>
                </UFormGroup>

                <UFormGroup label="Confirmar senha" name="confirmPassword">
                    <div class="relative mb-2">
                        <UInput :type="confirmPasswordVisible ? 'text' : 'password'" v-model="confirmPassword"
                            placeholder="Confirme sua senha" size="lg" required />
                        <button type="button" @click="togglePasswordVisibility('confirmPassword')"
                            :class="confirmPasswordVisible ? 'text-primary' : ''"
                            class="absolute inset-y-0 right-0 pr-3 flex items-center">
                            <UIcon :name="confirmPasswordVisible ? 'i-mdi-eye' : 'i-mdi-eye-off'" class="w-6 h-6" />
                        </button>
                    </div>
                    <transition enter-active-class="duration-500 ease-in opacity-0" enter-to-class="opacity-100"
                        leave-active-class="duration-500 ease-out" leave-class="opacity-100" leave-to-class="opacity-0">
                        <p v-if="passwordMismatch" class="text-red-500 text-sm mt-1 font-semibold">
                            As senhas não coincidem
                        </p>
                    </transition>
                </UFormGroup>

                <transition name="fade">
                    <UAlert v-show="showError" :title="'Erro ao realizar cadastro'" :description="errorMessage"
                        color="red" variant="subtle" />
                </transition>

                <div class="flex items-center justify-between">
                    <UButton block
                        class="bg-primary hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
                        type="submit" :disabled="!canSubmit">
                        Cadastrar
                    </UButton>
                </div>
            </form>
        </UCard>
    </UContainer>
</template>
<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import authService from "@/services/authService";
import { checkPasswordStrength, checkNameStrength, isEmailValid } from "@/utils/validatorsUtils";

const router = useRouter();
const name = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const passwordVisible = ref(false);
const confirmPasswordVisible = ref(false);
const showError = ref(false);
const errorMessage = ref("");
const isLoggedIn = ref(false);

const passwordMismatch = computed(
    () => password.value !== confirmPassword.value && confirmPassword.value !== ""
);

const togglePasswordVisibility = (field: "password" | "confirmPassword") => {
    if (field === "password") {
        passwordVisible.value = !passwordVisible.value;
    } else if (field === "confirmPassword") {
        confirmPasswordVisible.value = !confirmPasswordVisible.value;
    }
};

const strength = computed(() => checkPasswordStrength(password.value));
const score = computed(() => strength.value.filter((req) => req.met).length);

const color = computed(() => {
    if (score.value === 0) return undefined;
    if (score.value <= 1) return "red";
    if (score.value <= 2) return "yellow";
    if (score.value === 3) return "yellow";
    return "green";
});

const text = computed(() => {
    if (score.value === 0) return "Digite uma senha, ela deve conter:";
    if (score.value <= 2) return "Sua senha ainda está fraca, deve conter:";
    if (score.value === 3) return "Sua senha está quase lá, mas deve conter:";
    return "Agora sim! Sua senha está forte!";
});

const nameStrength = computed(() => checkNameStrength(name.value));
const nameScore = computed(() => nameStrength.value.filter((req) => req.met).length);

const nameColor = computed(() => {
    if (nameScore.value === 0) return "red";
    if (nameScore.value === 1) return "yellow";
    if (nameScore.value === 2) return "yellow";
    return "green";
});

const nameText = computed(() => {
    if (nameScore.value === 0) return "Digite um nome de usuário, ele deve conter:";
    if (nameScore.value <= 2)
        return "Seu nome de usuário ainda não atende aos requisitos, ele deve conter:";
    return "Agora sim! Seu nome de usuário está válido!";
});

const emailValid = computed(() => isEmailValid(email.value));

const canSubmit = computed(() => {
    return (
        nameScore.value === 3 &&
        emailValid.value &&
        score.value === 4 &&
        !passwordMismatch.value
    );
});

const onSubmit = async () => {
    if (!canSubmit.value) {
        showError.value = true;
        errorMessage.value = "Por favor, preencha todos os campos corretamente.";
        return;
    }

    try {
        await authService.register(name.value, email.value, password.value);
        router.push("welcome");
    } catch (error: any) {
        if (error instanceof Error) {
            errorMessage.value = error.message;
        } else {
            errorMessage.value = "Ocorreu um erro inesperado. Tente novamente.";
        }

        showError.value = true;
    }
};


onMounted(async () => {
    if (await authService.isLoggedIn()) {
        isLoggedIn.value = true;
        router.push("/");
    }
});
</script>