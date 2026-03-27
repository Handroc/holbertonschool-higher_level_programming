document.addEventListener('DOMContentLoaded', function () {
  const myurl = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const hello = document.querySelector('#hello');

  fetch(myurl)
    .then(response => {
      return response.json();
    })
    .then(data => {
      hello.textContent = data.hello;
    });
});
