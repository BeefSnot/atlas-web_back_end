process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write(`Your name is: ${chunk.toString().trim()}\n`);
  }
})

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
