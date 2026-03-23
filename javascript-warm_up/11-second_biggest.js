#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}

let biggest = process.argv[2];

for (let i = 3; i < process.argv.length; i++) {
  const b = process.argv[i + 1];
  if (b > biggest) {
    biggest = b;
  }
}

let biggest1 = process.argv[2];

for (let i = 3; i < process.argv.length; i++) {
  const b = process.argv[i + 1];
  if (!(b === biggest)) {
    if (b > biggest1) {
      biggest1 = b;
    }
  }
}

console.log(biggest1);
