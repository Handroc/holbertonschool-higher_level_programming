#!/usr/bin/node
if (Number.isNaN((Number(process.argv[2])))) {
  console.log('Missing number of occurrences');
} else {
  const d = Math.trunc(process.argv[2]);
  for (let i = d; i > 0; i--) {
    console.log('C is fun');
  }
}
