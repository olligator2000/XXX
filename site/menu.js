const catalogBtn = document.getElementById('catalogBtn');
const categories = document.getElementById('categories');

// Показать/скрыть каталог при наведении
catalogBtn.addEventListener('mouseenter', function() {
    categories.style.display = 'block';
});

categories.addEventListener('mouseleave', function() {
    categories.style.display = 'none';
});

// Закрыть меню при клике вне его
document.addEventListener('click', function(e) {
    if (!catalogBtn.contains(e.target) && !categories.contains(e.target)) {
        categories.style.display = 'none';
    }
});