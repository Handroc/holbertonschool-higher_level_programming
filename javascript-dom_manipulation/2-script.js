const clickheaders = document.querySelector('#red_header');

clickheaders.addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
