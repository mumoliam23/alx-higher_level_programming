#!/usr/bin/node

let fs = require('fs');
let file = process.argv[2];

function readPrint(file) {
  fs.readFile(file, 'utf-8', function(err, data) {
    if (err) {
      console.log("Error occurred while reading the file:", err);
    } else {
      console.log(data);
    }
  });
}

readPrint(file);

