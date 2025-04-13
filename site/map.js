// ymaps.ready(init);

// function init() {
//     var geolocation = ymaps.geolocation,
//         myPlacemark,
//         myMap = new ymaps.Map('map', {
//             center: [55.751574, 37.573856],
//             zoom: 8
//         }, {
//             searchControlProvider: 'yandex#search',
//             suppressMapOpenBlock: true
//         });

//     // Создаем кастомную метку (как в Яндекс.Еде)
//     function createPlacemark(coords) {
//         return new ymaps.Placemark(coords, {}, {
//             iconLayout: 'default#image',
//             iconImageHref: 'metka.png',
//             iconImageSize: [32, 32],
//             iconImageOffset: [-16, -32],
//             draggable: true
//         });
//     }

//     // Функция для определения адреса
//     function updateAddress() {
//         var center = myMap.getCenter();
        
//         ymaps.geocode(center, {
//             kind: 'house',
//             results: 1
//         }).then(function(res) {
//             var firstGeoObject = res.geoObjects.get(0);
            
//             if (!firstGeoObject) {
//                 return;
//             }
            
//             // Удаляем старую метку
//             if (myPlacemark) {
//                 myMap.geoObjects.remove(myPlacemark);
//             }
            
//             // Создаем новую метку
//             myPlacemark = createPlacemark(center);
//             myMap.geoObjects.add(myPlacemark);
            
//             // Формируем адрес
//             var address = [
//                 firstGeoObject.getThoroughfare() || firstGeoObject.getPremise(),
//                 firstGeoObject.getPremiseNumber()
//             ].filter(Boolean).join(', ');
            
//             // Обновляем свойства метки
//             myPlacemark.properties.set({
//                 iconCaption: address || 'Адрес не определен',
//                 balloonContent: firstGeoObject.getAddressLine()
//             });
            
//             // Можно использовать адрес для формы заказа
//             console.log('Выбранный адрес:', firstGeoObject.getAddressLine());
            
//         }).catch(function(err) {
//             console.error('Ошибка геокодирования:', err);
//         });
//     }

//     // Определяем местоположение пользователя
//     geolocation.get({
//         provider: 'browser',
//         mapStateAutoApply: true
//     }).then(function(result) {
//         myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 18);
//         updateAddress();
//     }).catch(function(error) {
//         geolocation.get({
//             provider: 'yandex'
//         }).then(function(result) {
//             myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 15);
//             updateAddress();
//         });
//     });

//     // Обновляем адрес при перемещении карты
//     myMap.events.add('boundschange', function(e) {
//         if (!e.get('newZoom') || e.get('newZoom') < 14) return;
//         updateAddress();
//     });

//     // Обновляем адрес при клике
//     myMap.events.add('click', function(e) {
//         myMap.setCenter(e.get('coords'));
//     });

//     // Инициализируем первый адрес
//     updateAddress();
// }

//+++++++++++++++++++++++

// ymaps.ready(init);

// function init() {
//     var geolocation = ymaps.geolocation,
//         myMap = new ymaps.Map('map', {
//             center: [55.751574, 37.573856],
//             zoom: 8
//         }, {
//             searchControlProvider: 'yandex#search',
//             suppressMapOpenBlock: true
//         });

//     // Функция для определения адреса
//     function updateAddress() {
//         var center = myMap.getCenter();
        
//         ymaps.geocode(center, {
//             kind: 'house',
//             results: 1
//         }).then(function(res) {
//             var firstGeoObject = res.geoObjects.get(0);
            
//             if (!firstGeoObject) {
//                 return;
//             }
            
//             // Формируем адрес
//             var address = [
//                 firstGeoObject.getThoroughfare() || firstGeoObject.getPremise(),
//                 firstGeoObject.getPremiseNumber()
//             ].filter(Boolean).join(', ');
            
//             // Можно использовать адрес для формы заказа
//             console.log('Выбранный адрес:', firstGeoObject.getAddressLine());
            
//         }).catch(function(err) {
//             console.error('Ошибка геокодирования:', err);
//         });
//     }

//     // Определяем местоположение пользователя
//     geolocation.get({
//         provider: 'browser',
//         mapStateAutoApply: true
//     }).then(function(result) {
//         myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 18);
//         updateAddress();
//     }).catch(function(error) {
//         geolocation.get({
//             provider: 'yandex'
//         }).then(function(result) {
//             myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 15);
//             updateAddress();
//         });
//     });

//     // Обновляем адрес при перемещении карты
//     myMap.events.add('boundschange', function(e) {
//         if (!e.get('newZoom') || e.get('newZoom') < 14) return;
//         updateAddress();
//     });

//     // Обновляем адрес при клике
//     myMap.events.add('click', function(e) {
//         myMap.setCenter(e.get('coords'));
//         updateAddress(); // Обновляем адрес при клике
//     });

//     // Инициализируем первый адрес
//     updateAddress();
// }


// var balloon = myPlacemark.properties.get('balloon');
//     document.getElementById('output').innerText = balloon;

// console.log(myPlacemark.properties.get('balloon'))



ymaps.ready(init);

function init() {
    var geolocation = ymaps.geolocation,
        myPlacemark,
        myMap = new ymaps.Map('map', {
            center: [55.751574, 37.573856],
            zoom: 15
        }, {
            searchControlProvider: 'yandex#search',
            suppressMapOpenBlock: true
        });

    // Функция для обновления вывода адреса
    function updateAddressOutput(address) {
        document.getElementById('output').textContent = address;
    }

    // Функция для определения адреса
    function updateAddress() {
        var center = myMap.getCenter();
        
        ymaps.geocode(center, {
            kind: 'house',
            results: 1
        }).then(function(res) {
            var firstGeoObject = res.geoObjects.get(0);
            
            if (!firstGeoObject) {
                updateAddressOutput('Адрес не определен');
                return;
            }
            
            // Удаляем старую метку
            if (myPlacemark) {
                myMap.geoObjects.remove(myPlacemark);
            }
            
            // Создаем новую ПРОЗРАЧНУЮ метку
            myPlacemark = new ymaps.Placemark(center, {}, {
                iconLayout: 'default#image',
                iconImageHref: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"></svg>', // Прозрачная SVG
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -32],
                draggable: false
            });
            myMap.geoObjects.add(myPlacemark);
            
            // Получаем полный адрес
            var fullAddress = firstGeoObject.getAddressLine();
            
            // Устанавливаем свойства метки
            myPlacemark.properties.set({
                iconCaption: '', // Убираем подпись
                balloonContent: fullAddress
            });
            
            // Выводим адрес в div
            updateAddressOutput(fullAddress);
            
        }).catch(function(err) {
            console.error('Ошибка геокодирования:', err);
            updateAddressOutput('Ошибка определения адреса');
        });
    }

    // Определяем местоположение пользователя
    geolocation.get({
        provider: 'browser',
        mapStateAutoApply: true
    }).then(function(result) {
        myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 17);
        updateAddress();
    }).catch(function(error) {
        geolocation.get({
            provider: 'yandex'
        }).then(function(result) {
            myMap.setCenter(result.geoObjects.get(0).geometry.getCoordinates(), 15);
            updateAddress();
        });
    });

    // Обновляем адрес при изменении карты (с задержкой)
    var updateTimer;
    myMap.events.add(['boundschange', 'actionend'], function(e) {
        if (e.get('newZoom') && e.get('newZoom') < 14) return;
        clearTimeout(updateTimer);
        updateTimer = setTimeout(updateAddress, 300);
    });

    // Обновляем адрес при клике
    myMap.events.add('click', function(e) {
        myMap.panTo(e.get('coords'), {
            flying: true,
            duration: 300
        });
    });

    // Первоначальное обновление
    updateAddress();
}