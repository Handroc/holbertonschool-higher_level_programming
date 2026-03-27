const myurl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.querySelector('#character');

fetch(myurl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    character.textContent = data.name;
  });
