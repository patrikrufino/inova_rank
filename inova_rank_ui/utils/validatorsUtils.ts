export function checkPasswordStrength(password: string) {
  const requirements = [
    { regex: /.{8,}/, text: "Pelo menos 8 caracteres" },
    { regex: /\d/, text: "Pelo menos 1 número" },
    { regex: /[a-z]/, text: "Pelo menos 1 letra minúscula" },
    { regex: /[A-Z]/, text: "Pelo menos 1 letra maiúscula" },
  ];

  return requirements.map((req) => ({
    met: req.regex.test(password),
    text: req.text,
  }));
}

export function checkNameStrength(name: string) {
  const requirements = [
    { regex: /^.{3,}$/, text: "Deve ter no mínimo 3 caracteres" },
    { regex: /^[a-zA-Z]/, text: "Deve começar com uma letra" },
    { regex: /^[a-zA-Z0-9]*$/, text: "Não pode conter símbolos" },
  ];

  return requirements.map((req) => ({
    met: req.regex.test(name),
    text: req.text,
  }));
}

export function isEmailValid(email: string): boolean {
  if (email.trim() === "") return true;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
