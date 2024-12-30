#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

function fetchMovieCharacters() {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching the movie:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);

    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character:', error);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  });
}

fetchMovieCharacters();
