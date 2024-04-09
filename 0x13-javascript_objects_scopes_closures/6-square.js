#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
        this.print(c)
    } else {
        this.print();
    }
  }
}

module.exports = Square;
