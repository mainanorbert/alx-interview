const request = require('request');

const getStarWarsCharacters = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error retrieving movie data: ${error}`);
      return;
    }

    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      const characters = data.characters;

      if (characters) {
        characters.forEach((characterUrl) => {
          request(characterUrl, (characterError, characterResponse, characterBody) => {
            if (characterError) {
              console.error(`Error retrieving character data: ${characterError}`);
              return;
            }

            if (characterResponse.statusCode === 200) {
              const characterData = JSON.parse(characterBody);
              console.log(characterData.name);
            } else {
              console.error(`Error retrieving character data: ${characterResponse.statusCode}`);
            }
          });
        });
      } else {
        console.log("No characters found for this movie.");
      }
    } else {
      console.error(`Error retrieving movie data: ${response.statusCode}`);
    }
  });
};

// Get movie ID from command line argument (assuming script is run as node script.js movie_id)
const movieId = process.argv[2];

if (movieId) {
  getStarWarsCharacters(parseInt(movieId));
} else {
  console.error("Please provide a movie ID as an argument.");
}

