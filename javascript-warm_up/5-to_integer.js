#!/usr/bin/node
if (Number.isNaN((Number(process.argv[2])))) {
  console.log('Not a number');
} else {
  const num = Math.trunc(process.argv[2]);
  console.log('My number:', num);
}
