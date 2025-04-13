//Доп. окно для карты

const output = document.getElementById('output');
const mapModal = document.getElementById('map-modal');

output.addEventListener('click', function() {
    mapModal.style.display = 'flex'; // Показываем модальное окно
});

function closeMap() {
    mapModal.style.display = 'none'; // Скрываем модальное окно
}