#!/usr/bin/node
let arg = process.argv;
if (arg[2] === null) {
    console.log("Not a number")
}
else if (!parseInt(arg[2])) {
    console.log("Not a number")
}
else if (arg[2]){
    console.log("My number: " + parseInt(arg[2]))
}
