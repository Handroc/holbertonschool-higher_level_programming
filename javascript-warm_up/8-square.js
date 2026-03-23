#!/usr/bin/node
const size = process.argv[2];
if (Number.isNaN((Number(size)))) {
  console.log('Missing size');
} else {
  const d = Math.trunc(process.argv[2]);
  for (let j = d; j > 0; j--) {
    let line = '';
    for (let i = d; i > 0; i--) {
      line += 'X';
    }
    console.log(line);
  }
}
