const myurl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const my_list = document.querySelector('#list_movies');

fetch(myurl)
  .then(response =>{
    return response.json();
  })
  .then(data =>{
    for (const item of data.results) {
        my_list.append(item.title);
    }
  })
