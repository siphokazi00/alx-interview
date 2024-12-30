#!/usr/bin/node
const axios = require("axios");

async function getMovieCharacters(movieId) {
  const baseUrl = "https://swapi-api.alx-tools.com/api/films/";

  try {
    const movieResponse = await axios.get(`${baseUrl}${movieId}/`);
    const movieData = movieResponse.data;

    const characters = movieData.characters;

    for (const characterUrl of characters) {
      try {
        const characterResponse = await axios.get(characterUrl);
        const characterData = characterResponse.data;
        console.log(characterData.name);
      } catch (err) {
        console.error(`Error fetching character: ${characterUrl}`);
      }
    }
  } catch (err) {
    console.error("Error fetching movie data:", err.message);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error("Usage: node star_wars_characters.js <Movie ID>");
  process.exit(1);
}

getMovieCharacters(movieId);
