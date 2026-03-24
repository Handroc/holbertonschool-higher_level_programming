const clickheaders = document.querySelector('#red_header');
const headers = document.querySelector('header');

clickheaders.addEventListener('click', function () {
  headers.classList.add('red');
});
