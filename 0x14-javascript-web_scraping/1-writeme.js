#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node script_name.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function(err) {
  if (err) {
    console.error("Error occurred while writing to the file:", err);
  }
});

