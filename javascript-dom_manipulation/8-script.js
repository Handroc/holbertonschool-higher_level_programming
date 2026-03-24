const myurl = 'https://hellosalut.stefanbohacek.com/?lang=fr';
const my_list = document.querySelector('#hello');

fetch(myurl)
  .then(response =>{
    return response;
  })
  .then(data =>{
    my_list.append(data.hello);
  })
