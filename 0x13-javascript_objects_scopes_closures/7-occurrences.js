#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let num of list) {
    if (num === searchElement) {
      count++;
    }
  }
  return count;
};
