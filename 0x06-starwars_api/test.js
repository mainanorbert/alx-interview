#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie data:', error);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  console.log(`Characters in ${movie}:`);

  const fetchCharacters = (charactersUrls) => {
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Failed to fetch character data:', error);
          return;
        }

        const character = JSON.parse(body);
        // console.log(`- ${character.name}`);
      });
    });
  };

  fetchCharacters(movie.characters);
});

