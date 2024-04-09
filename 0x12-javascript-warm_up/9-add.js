#!/usr/bin/node
function add (a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);
  const result = numA + numB;
  console.log(result);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Missing size');
  return;
}
add(arg1, arg2);
