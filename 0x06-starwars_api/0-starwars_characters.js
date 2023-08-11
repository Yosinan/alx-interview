#!/usr/bin/node

// require - Imports a module
const request = require('request');
// import request from 'request';
// getMovieCharacters - Prints all characters of a Star Wars movie
function getMovieCharacters (movieId) {
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  request(filmUrl, (error, response, filmData) => {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(filmData);

      const characterUrls = film.characters;

      const characterPromises = characterUrls.map((characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, characterData) => {
            if (!error && response.statusCode === 200) {
              const character = JSON.parse(characterData);
              resolve(character.name);
            } else {
              resolve(
                `Failed to fetch character data for URL: ${characterUrl}`
              );
            }
          });
        });
      });

      Promise.all(characterPromises).then((characterNames) => {
        characterNames.forEach((characterName) => console.log(characterName));
      });
    } else {
      console.error(`Failed to fetch film data for ID: ${movieId}`);
    }
  });
}

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('Usage: star_wars_characters_request.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
getMovieCharacters(movieId);
