#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    process.exit(1);
  }
  const urls = JSON.parse(body).characters;
  function makeRequests (urls) {
    if (urls.length === 0) {
      return;
    }
    const url = urls.shift(); // Get the first URL
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      makeRequests(urls);
    });
  }
  makeRequests(urls);
});
