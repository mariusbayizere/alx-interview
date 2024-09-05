#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieID = process.argv[2];

// Define the URL for the Star Wars API film endpoint with the movie ID
const url = `https://swapi.dev/api/films/${movieID}/`;

// Request the film data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Function to fetch and print character names in order
  const printCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const charData = JSON.parse(charBody);
      console.log(charData.name);
      printCharacter(index + 1);
    });
  };

  // Start printing characters
  printCharacter(0);
});
