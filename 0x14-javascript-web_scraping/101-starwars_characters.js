#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

//  the 'request' module to perform an HTTP GET request to the Star Wars API URL.
request(apiUrl, function (error, response, body) {
  // Check if there was no error during the HTTP request
  if (!error && response.statusCode === 200) {
    // Parse the JSON response bod
    const movieData = JSON.parse(body);
    // create an array of promises that fetch the data for each individual character.
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // Use another 'request' to fetch the data for the individual character.
        request(characterUrl, function (charError, charResponse, charBody) {
          // Check if there was no error during the HTTP request
          if (!charError && charResponse.statusCode === 200) {
            // Parse the JSON response body
            const characterData = JSON.parse(charBody);
            // Resolve the promise with the name of the character.
            resolve(characterData.name);
          } else {
            // reject the promise with the error message if  there was an error during the HTTP request
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});

