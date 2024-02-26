document.addEventListener('DOMContentLoaded', function() {
    var searchBar = document.getElementById('search-bar');
  
    searchBar.addEventListener('input', function() {
      var searchValue = searchBar.value.toLowerCase();
      var letterItems = document.getElementsByClassName('letter-item');
  
      for (var i = 0; i < letterItems.length; i++) {
        var letterItem = letterItems[i];
        var nameElement = letterItem.getElementsByClassName('letter-item-text')[0];
        var name = nameElement ? nameElement.innerText.toLowerCase() : '';
  
        if (name.includes(searchValue)) {
          letterItem.style.display = 'block';  // Показываем элемент, если найдено соответствие
        } else {
          letterItem.style.display = 'none';   // Скрываем элемент, если нет соответствия
        }
      }
    });
});