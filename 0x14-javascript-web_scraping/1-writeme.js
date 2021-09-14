#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(str);
});
