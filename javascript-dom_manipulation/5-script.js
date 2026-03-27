const header = document.querySelector('header');
const clickheaders = document.querySelector('#update_header');

clickheaders.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
