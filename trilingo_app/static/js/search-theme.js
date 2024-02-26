const searchInput = document.getElementById('search-bar');

// Получаем ссылки на элементы, которые нужно фильтровать
const letterItems = document.getElementsByClassName('letter-item');

// Функция для фильтрации элементов в соответствии с введенным текстом
function filterItems() {
    const searchText = searchInput.value.toLowerCase();

    // Проходимся по всем элементам и скрываем те, которые не соответствуют поисковому запросу
    for (let i = 0; i < letterItems.length; i++) {
        const itemText = letterItems[i].querySelector('.letter-item-text').textContent.toLowerCase();
        if (itemText.includes(searchText)) {
            letterItems[i].style.display = 'block';
        } else {
            letterItems[i].style.display = 'none';
        }
    }
}

filterItems()