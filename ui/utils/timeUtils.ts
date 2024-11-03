export const timeAgo = (date: string): string => {
  const now = new Date();
  const seconds = Math.floor((now.getTime() - new Date(date).getTime()) / 1000);
  let interval = Math.floor(seconds / 31536000);

  if (interval > 1) return `${interval} anos atrás`;
  interval = Math.floor(seconds / 2592000);
  if (interval > 1) return `${interval} meses atrás`;
  interval = Math.floor(seconds / 86400);
  if (interval > 1) return `${interval} dias atrás`;
  interval = Math.floor(seconds / 3600);
  if (interval > 1) return `${interval} horas atrás`;
  interval = Math.floor(seconds / 60);
  if (interval > 1) return `${interval} minutos atrás`;
  return `${seconds} segundos atrás`;
};