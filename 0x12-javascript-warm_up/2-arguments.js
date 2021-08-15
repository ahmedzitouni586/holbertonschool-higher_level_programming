#!/usr/bin/node
// print a message depending of the number of arguments passed
const arg = process.argv;
const len = arg.length;
if (len === 2) {
    console.log("No argument");
}
else if (len === 3) {
    console.log('Argument found');
}
else {
    console.log("Arguments found");
}
