#!/usr/bin/node
const nSquare = require('./5-square');
module.exports = class Square extends nSquare {
  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.width; ++i) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
