#!/usr/bin/env node

import fetch from 'node-fetch';

async function getMovieCharacters(movieId) {
    try {
        const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
        const filmResponse = await fetch(filmUrl);
        const film = await filmResponse.json();

        const characterUrls = film.characters;
        const characterPromises = characterUrls.map(async characterUrl => {
            try {
                const characterResponse = await fetch(characterUrl);
                const characterData = await characterResponse.json();
                return characterData.name;
            } catch (error) {
                return `Failed to fetch character data for URL: ${characterUrl}`;
            }
        });

        const characterNames = await Promise.all(characterPromises);
        characterNames.forEach(characterName => console.log(characterName));
    } catch (error) {
        console.error(`Failed to fetch film data for ID: ${movieId}`);
    }
}

const args = process.argv.slice(2);

if (args.length !== 1) {
    console.log('Usage: star_wars_characters_request.js <movie_id>');
    process.exit(1);
}

const movieId = args[0];
getMovieCharacters(movieId);

