// Задание 1:
/* Подсчитать сумму всех чисел в заданном пользователем
диапазоне. */

/* 
var min = +prompt('Задайте нижнюю границу');
var max = +prompt('Задайте верхнюю границу');
var sum = 0;

if (min >= max) {
    alert('Как-то странно')
} else {
    while (min <= max) {
        sum += min;
        min++;
    }
}

alert('Сумма последовательности ' + sum);
*/

// Задание 2:
/* Запросить 2 числа и найти только наибольший общий
делитель. */


var firstnumber = +prompt('Задайте первое число');
var secondnumber = +prompt('Задайте второе число');
var delit = 0;

if (firstnumber <= 0 || secondnumber <= 0) {
    alert('Числа должны быть больше нуля');
} else {
    for (var i = 1; (firstnumber <= secondnumber) ? i <= firstnumber : i <= secondnumber; i++) {
        if (firstnumber % i == 0 && secondnumber % i == 0) {
            delit = i;
        }
    }
    alert('НОД у чисел ' + firstnumber + ' и ' + secondnumber + ' = ' + delit);
}


// Задание 3:
/* Запросить у пользователя число и вывести все делители
этого числа. */

/* 
var number = +prompt('Ваше число?');
var result = ''

for (var i = 1; i <= number; i++) {
    if (number % i == 0) {
        result += ' ' + i;
    }
}

alert(result);
*/

// Задание 4:
/* Определить количество цифр в введенном числе. */

/* 
var index = 0;
var num = number;

if (number == 0) {
    index = 1;
}

while (number >= 1) {
    number /= 10;
    index++;
}

alert('Кол-во цифр в ' + num + ' = ' + index);
*/

// Задание 5:
/* Запросить у пользователя 10 чисел и подсчитать, сколько
он ввел положительных, отрицательных и нулей. При этом
также посчитать, сколько четных и нечетных. Вывести
статистику на экран. Учтите, что достаточно одной пере-
менной (не 10) для ввода чисел пользователем. */

/*
var positive = negative = zero = even = odd = 0;

for (var i = 1; i <= 10; i++) {
    var variable = +prompt('Введите число');
    if (variable > 0) {
        positive++;
        variable % 2 == 0 ? even++ : odd++;
    } else if (variable < 0) {
        negative++;
        variable % 2 == 0 ? even++ : odd++;
    } else {
        zero++;
    }
}

alert('Кол-во положительных = ' + positive + '\n' + 'Кол-во отрицательных = ' + negative + '\n' + 'Кол-во нулей = ' + zero + '\n' + 'Кол-во четных = ' + even + '\n' + 'Кол-во нечетных = ' + odd);
*/

// Задание 6:
/* Зациклить калькулятор. Запросить у пользователя 2 числа
и знак, решить пример, вывести результат и спросить, хо-
чет ли он решить еще один пример. И так до тех пор, пока
пользователь не откажется. */

/*
while (true) {
    var firstnumber = +prompt('Задайте первое число');
    var secondnumber = +prompt('Задайте второе число');
    var symbol = prompt('Введите знак');
    var result = 0;

    switch (symbol) {
        case '+':
            result = firstnumber + secondnumber;
            alert(firstnumber + ' + ' + secondnumber + ' = ' + result);
            break;
        case '-':
            result = firstnumber - secondnumber;
            alert(firstnumber + ' - ' + secondnumber + ' = ' + result);
            break;
        case '*':
            result = firstnumber * secondnumber;
            alert(firstnumber + ' * ' + secondnumber + ' = ' + result);
            break;
        case '/':
            if (secondnumber == 0) {
                alert('Не хочу делить на ноль');
                break;
            }
            result = firstnumber / secondnumber;
            alert(firstnumber + ' / ' + secondnumber + ' = ' + result);
            break;
        default:
            alert('Не понял');
            break;
    }

    otvet = confirm('Хотите продолжить?');
    if (otvet == false) {
        break;
    }
}
*/

// Задание 7:
/* Запросить у пользователя число и на сколько цифр его
сдвинуть. Сдвинуть цифры числа и вывести результат (если
число 123456 сдвинуть на 2 цифры, то получится 345612). */

/*
var number = prompt('Введите число').split('');
var index = +prompt('Сдвиг');

for (var i = 0; i < index; i++) {
    var first = number[0];
    for (var j = 1; j < number.length; j++) {
        number[j-1] = number[j];
        number[j] = number[j+1];
    }
    number[number.length-1] = first;
}

alert(number.join(''));
*/

// Задание 8:
/* Зациклить вывод дней недели таким образом: «День недели.
Хотите увидеть следующий день?» и так до тех пор, пока
пользователь нажимает OK. */

/*
while (true) {
    var day = confirm('Понедельник. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Вторник. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Среда. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Четверг. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Пятница. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Суббота. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
    var day = confirm('Воскресенье. Хотите увидеть следующий день?');
    if (day == false) {
        break;
    }
}
*/

// Задание 9:
/* Вывести таблицу умножения для всех чисел от 2 до 9.
Каждое число необходимо умножить на числа от 1 до 10. */

/*
var table = '';

for (var i = 1; i <= 10; i++) {
    for (var j = 2; j <= 9; j++) {
        table += i*j + '          '; 
    }
    table += '\n';
}

alert(table);
*/

// Задание 10:
/* Игра «Угадай число». Предложить пользователю загадать
число от 0 до 100 и отгадать его следующим способом:
каждую итерацию цикла делите диапазон чисел пополам,
записываете результат в N и спрашиваете у пользователя
«Ваше число > N, < N или == N?». В зависимости от того
что указал пользователь, уменьшаете диапазон. Начальный
диапазон от 0 до 100, поделили пополам и получили 50.
Если пользователь указал, что его число > 50, то изменили
диапазон на от 51 до 100. И так до тех пор, пока пользова-
тель не выберет == N. */

// alert('Загадай число от 0 до 100');

// var min = 0;
// var max = 100;
// var n = 50;

// while (true) {
//     alert('Ваше число >, < или = ' + n);
//     var answer = prompt();
//     switch (answer) {
//         case '>':
//             min = n + 1;
//             n = Math.ceil((max + min) / 2);
//             continue;
//         case '<':
//             max = n - 1;
//             n = Math.ceil((min + max) / 2);
//             continue;
//         case '=':
//             alert('ваше число ' + n)
//             break;
//         default:
//             alert('Не подходит')
//             continue;
//     }
//     break;
// }
