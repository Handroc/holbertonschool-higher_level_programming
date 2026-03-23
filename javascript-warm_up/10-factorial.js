#!/usr/bin/node
function factorial (a) {
  a = Number(a);
  if (Number.isNaN(a) || a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(process.argv[2]));
