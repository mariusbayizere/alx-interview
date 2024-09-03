#!/usr/bin/node

const request = require('request');

// The movie ID is passed as the first command-line argument
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Create an empty array to store character names
    const characterNames = [];

    // Function to get character names
    const getCharacterName = (url, index) => {
      request(url, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          characterNames[index] = character.name;

          // Once all characters have been fetched, print them
          if (characterNames.length === characters.length) {
            characterNames.forEach(name => {
              console.log(name);
            });
          }
        }
      });
    };

    // Fetch each character name
    characters.forEach((characterUrl, index) => {
      getCharacterName(characterUrl, index);
    });
  }
});
