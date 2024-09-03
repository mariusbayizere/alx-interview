#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, response, body) => {
    if (err) {
      console.error(err);
      return;  // Stop execution if an error occurs
    }

    const charactersURL = JSON.parse(body).characters;
    const characterPromises = charactersURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, res, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            } else {
              resolve(JSON.parse(charactersReqBody).name);
            }
          });
        })
    );

    Promise.all(characterPromises)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.error(allErr));
  });
}
