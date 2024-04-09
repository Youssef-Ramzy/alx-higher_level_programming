#!/usr/bin/node
let list = [1, 2, 3, 4, 5];
console.log(list);
list = list.map((value, index) => value * index);
console.log(list);
