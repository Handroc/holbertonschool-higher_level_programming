const headers = document.querySelector('header');
const clickheaders = document.querySelector('#toggle_header');

clickheaders.addEventListener('click', function () {
  if (headers.classList.contains('red')) {
    headers.classList.remove('red');
    headers.classList.add('green');
  } else {
    headers.classList.remove('green');
    headers.classList.add('red');
  }
});
