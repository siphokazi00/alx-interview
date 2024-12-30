#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
  const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(baseUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error.message);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
      return;
    }

    try {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(`Error fetching character: ${characterUrl}`);
            return;
          }

          if (charResponse.statusCode === 200) {
            try {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } catch (parseError) {
              console.error('Error parsing character data:', parseError.message);
            }
          } else {
            console.error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing movie data:', parseError.message);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node star_wars_characters.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
