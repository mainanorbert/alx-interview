const request = require('request');

const urls = [
  'https://swapi.dev/api/people/1/',
  'https://swapi.dev/api/people/2/',
  'https://swapi.dev/api/people/3/',
  'https://swapi.dev/api/people/4/',
  'https://swapi.dev/api/people/5/',
  'https://swapi.dev/api/people/10/',
  'https://swapi.dev/api/people/13/',
  'https://swapi.dev/api/people/14/',
  'https://swapi.dev/api/people/16/',
  'https://swapi.dev/api/people/18/',
  'https://swapi.dev/api/people/20/',
  'https://swapi.dev/api/people/21/',
  'https://swapi.dev/api/people/22/',
  'https://swapi.dev/api/people/25/',
  'https://swapi.dev/api/people/27/',
  'https://swapi.dev/api/people/28/',
  'https://swapi.dev/api/people/29/',
  'https://swapi.dev/api/people/30/',
  'https://swapi.dev/api/people/31/',
  'https://swapi.dev/api/people/45/'
];

// Function to make request to each URL in order
function makeRequests(urls) {
  if (urls.length === 0) {
    return;
  }

  const url = urls.shift(); // Get the first URL
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Parse the JSON response body
    const character = JSON.parse(body);

    // Print the character name
    console.log(character.name);

    // Make the next request
    makeRequests(urls);
  });
}

// Start making requests
makeRequests(urls);

