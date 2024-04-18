#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    process.exit(1);
  }
  const charactersUrls = JSON.parse(body).characters;
  charactersUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        process.exit(1);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
