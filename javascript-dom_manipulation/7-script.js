const myurl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.querySelector('#list_movies');

fetch(myurl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    for (const item of data.results) {
      const listItem = document.createElement('li');
      listItem.textContent = item.title;
      movieList.appendChild(listItem);
    }
  });
