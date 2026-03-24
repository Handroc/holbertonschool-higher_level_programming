const my_list = document.querySelector('ul.my_list');
const clickheaders = document.querySelector('#add_item');

clickheaders.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  my_list.appendChild(newItem);
});
