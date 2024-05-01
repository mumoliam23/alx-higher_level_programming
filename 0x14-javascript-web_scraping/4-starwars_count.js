#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
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
    let moviesWithCharacter = 0;
    const fetchCharacterDetails = (url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error('Error fetching character data:', error);
          return;
        }
        try {
          const characterData = JSON.parse(body);
          if (characterData && characterData.name === 'Wedge Antilles') {
            moviesWithCharacter++;
          }
        } catch (parseError) {
          console.error('Error parsing character data:', parseError);
        }
      });
    };
    data.results.forEach(film => {
      film.characters.forEach(characterUrl => {
        fetchCharacterDetails(characterUrl);
      });
    });
    // Adding a timeout to ensure all character details are fetched before logging
    setTimeout(() => {
      console.log(moviesWithCharacter);
    }, 2000); // You might need to adjust the timeout based on the API response time
  } catch (parseError) {
    console.error('Error parsing data:', parseError);
  }
});
