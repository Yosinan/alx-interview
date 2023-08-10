// #!/usr/bin/node

// // require - Imports a module
// const request = require('request');

// // getMovieCharacters - Prints all characters of a Star Wars movie
// function getMovieCharacters (movieId) {
//   const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

//   request(filmUrl, (error, response, filmData) => {
//     if (!error && response.statusCode === 200) {
//       const film = JSON.parse(filmData);
//       console.log(`Characters in ${film.title}:`);

//       const characterUrls = film.characters;

//       const characterPromises = characterUrls.map((characterUrl) => {
//         return new Promise((resolve, reject) => {
//           request(characterUrl, (error, response, characterData) => {
//             if (!error && response.statusCode === 200) {
//               const character = JSON.parse(characterData);
//               resolve(character.name);
//             } else {
//               resolve(
//                 `Failed to fetch character data for URL: ${characterUrl}`
//               );
//             }
//           });
//         });
//       });

//       Promise.all(characterPromises).then((characterNames) => {
//         characterNames.forEach((characterName) => console.log(characterName));
//       });
//     } else {
//       console.error(`Failed to fetch film data for ID: ${movieId}`);
//     }
//   });
// }

// const args = process.argv.slice(2);

// if (args.length !== 1) {
//   console.log('Usage: star_wars_characters_request.js <movie_id>');
//   process.exit(1);
// }

// const movieId = args[0];
// getMovieCharacters(movieId);

#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
