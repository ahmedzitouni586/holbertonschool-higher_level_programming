#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs-utf-8');

fs.readFile(process.argv[2], function (err, data) {
  if (err) console.log(err);
  else process.stdout.write(data);
});