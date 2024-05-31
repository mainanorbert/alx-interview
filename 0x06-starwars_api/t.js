const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the SWAPI film endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the SWAPI film endpoint
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const film = JSON.parse(body);

  // Print the characters list
  film.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the JSON response body
      const character = JSON.parse(body);

      // Print the character name
      console.log(character.name);
    });
  });
});

