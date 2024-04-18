#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const charactersUrls = JSON.parse(body).characters;
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          process.exit(1);
        }
        if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
