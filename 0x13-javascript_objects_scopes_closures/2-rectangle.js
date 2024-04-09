#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {

    } else if (!w || !h) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;