export function taskFirst() {
  return `I prefer const when I can.`;
}

export function getLast() {
  const ending = ' is okay';
  return ending;
}

export function taskNext() {
  const start = 'But sometimes let';
  return `${start}${getLast()}`;
}