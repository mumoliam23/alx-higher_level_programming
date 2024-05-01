#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

if (!apiUrl) {
  console.error('Error: No API URL provided!');
  process.exit(1);
}
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }
  try {
    const data = JSON.parse(body);
    if (!data || !Array.isArray(data.results)) {
      console.error('Error: Unable to retrieve valid data from the API.');
      return;
    }
    const moviesWithCharacter = data.results.filter(film => {
      return film.characters.includes(`${characterId}`);
    }).length;
    console.log(moviesWithCharacter);
  } catch (parseError) {
    console.error('Error parsing data:', parseError);
  }
});
