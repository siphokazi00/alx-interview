#!/usr/bin/node
const request = require('request');

// Get the movie ID from the first command-line argument
const movieID = process.argv[2];

// Define the URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Function to fetch and display the characters of the movie
function fetchMovieCharacters() {
  // Make a request to the Star Wars API for the specific movie
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching the movie:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      return;
    }

    // Parse the movie data from the API response
    const movieData = JSON.parse(body);

    // Get the characters array from the movie data
    const characters = movieData.characters;

    // Loop through the characters and fetch each one by URL
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character:', error);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          // Print the character name
          console.log(characterData.name);
        }
      });
    });
  });
}

// Execute the function to fetch and display characters
fetchMovieCharacters();

