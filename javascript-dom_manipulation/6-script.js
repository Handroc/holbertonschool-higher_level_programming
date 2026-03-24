const myurl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const my_list = document.querySelector('#character');

fetch(myurl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    my_list.append(data.name);
  })
