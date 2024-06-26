#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Error: URL is not provided');
  process.exit(1);
}
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else {
    if (response && response.statusCode) {
      console.log('code:', response.statusCode);
    } else {
      console.error('Error:', error);
      process.exit(1);
    }
  }
});
