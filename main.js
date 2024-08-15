// var x = +prompt("Введите X");
// if (x >= 0 && x <= 100) {
//   alert(x +  " - принадлежит 0...100");
// } else if (x >= 101 && x <= 1000)  {
//   alert(x +  " - принадлежит 101...1000");
// } else {
//     alert(x +  " - не принадлежит ничему");
// }
// ------------------------------

// var x = Number(prompt("Введите X"));
// var y = Number(prompt("Введите Y"));
// if (x > y) {
//     alert("x > y");
// } else if (x < y) {
//     alert("x < y");
// } else {
//     alert("x = y");
/// ------------------------------

// var x = Number(prompt("Введите X"));
// switch(x) {
//     case 0:
//         alert("ноль");
//         break;
//     case 1:
//         alert("один");
//         break;
//     case 2:
//         alert("два");
//         break;
//     case 3:
//         alert("три");
//         break;
//     case 4:
//         alert("четыре");
//         break;
//     case 5:
//         alert("пять");
//         break;
//     case 6:
//         alert("шесть");
//         break;
//     case 7:
//         alert("семь");
//         break;
//     case 8:
//         alert("восемь");
//         break;
//     case 9:
//         alert("девять");
//         break;
//     default:
//         alert("ничего");
//         break;
// }

// ------------------------------
// var n = +prompt("Введите количество решёток");

// while (n >= 0) {
//     console.log(n);
//     n--;
// }
// ------------------------------
// var n = +prompt("Введите число");
// var y = +prompt("Введите степень");
// var i = 0;
// var result  = 1;
// while (i < y) {
//     result*=n;
//     i++;
// }
// console.log(result);
// ------------------------------

// do {
//     var answer = +prompt("Введите ответ на пример 2+2*2");
// } while (answer != 6) 
// alert("Малорик")

// ------------------------------
// var n = +prompt("Введите число");
// for (i=1; i<=100; i++) {
//     if (i % n == 0) { 
//         console.log(i);
//     }
// }
// ------------------------------
// var x = +prompt('Задайте первое число');
// var y = +prompt('Задайте второе число');
// var delitel = 0;

// if (x <= 0 || y <= 0) {
//     alert('Числа должны быть больше нуля');
// } else {
//     for (var i = 1; (x <= y) ? i <= x : i <= y; i++) {
//         if (x % i == 0 && y % i == 0) {
//             delitel = i;
//             console.log('НОД у чисел ' + x + ' и ' + y + ' = ' + delitel);
//         }
//     }
//     alert('НОД у чисел ' + x + ' и ' + y + ' = ' + delitel);
// }
// ------------------------------
// var x = +prompt('Задайте первое число');
// var y = +prompt('Задайте второе число');
// var delitel = 0;
// var i = 1;


// if (x <= 0 || y <= 0) {
//     alert('Числа должны быть больше нуля');
// } else if (x <= y) {
//     i <= x;
//     while (x % i !== 0 && y % i !== 0) {
//         i++;
//     }

// } else if (x >= y) {
//     i <= y;
//     while (x % i !== 0 && y % i !== 0) {
//         i++;
//     }
//     alert('НОД у чисел ' + x + ' и ' + y + ' = ' + delitel);
// }
// ----------------------Задание 6      
        // Зациклить калькулятор. Запросить у пользователя 2 числа и знак, решить пример, вывести результат и спросить, хочет ли он решить еще один пример. И так до тех пор, пока пользователь не откажется.
        // var answer = 0;
        // var del = String("/");
        // var umn = String("*");
        // var minus = String("-");
        // var plus = String("+");
        // while (true) { 
        // var x = parseInt(prompt("Введите первое число"));
        // if (isNaN(x)) {
        //     alert("Вы ввели не число!");
        // } else {
        //     var symbol = String(prompt("Введите операцию '/' или '*' или '-' или '+'"));
        //     // var operators = String(symbol);
        //     if ((symbol !== del) && (symbol !== umn) && (symbol !== minus) && (symbol !== plus)) {
        //         alert("Вы ввели неверный оператор!");
        //     } else {
        //         var y = parseInt(prompt("Введите второе число"));
        //         if (isNaN(y)) {
        //             alert("Вы ввели не число!")
        //         } else if(symbol == "/") {
        //             if(y == 0)
        //         answer =  x / y
        //         } else if(symbol == "*") {
        //         answer =  x * y
        //         } else if(symbol == "-") {
        //         answer =  x - y
        //         } else if(symbol == "+") {
        //         answer =  x + y
        //         }
        //         alert(answer);                
        //         } 
        //     if (confirm("Хотите еще решить пример?")) {
        //             continue;
        //         } else {
        //             break;
        //         }
        //     }
        // }



// ----------------------
//Запросить у пользваотеля 2 числа, вывести среднее арифметическое
// var x = parseInt(prompt("Введите первое число"));
// var y = parseInt(prompt("Введите второе число"));
// var answer = x * y / 2;
// alert("Среднее арифметеческое чисел " + x " и " + у + " равна " + answer);
// ----------------------
//Запросить у пользваотеля 2 числа, вывести площадь, периметр и длину диагонали прямоугольника
// var x = parseInt(prompt("Введите длину первой стороны"));
// var y = parseInt(prompt("Введите длину второй стороны"));
// var s = x * y;
// var p = (x * 2) + (y * 2);
// var d = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
// alert("Площадь равна " + s + " Периметр равен " + p + " Диагональ равна " + d);
// ----------------------
//Дана окружность с центром 0, 0 и радиусом R.
//Пользователь вводит координаты точки.
//Вывести на экран одно из сообщений: Точка лежит внутри окружности, Точка лежит на окружности, Точка лежит снаружи.
// var x = parseInt(prompt("Введите первую координату точки"));
// var y = parseInt(prompt("Введите вторую координату точки"));
// var r = parseInt(prompt("Введите радиус"));
// var radius = Math.sqrt((Math.pow(x, 2) - Math.pow(0, 2)) + (Math.pow(y, 2) - Math.pow(0, 2)));
// if(radius > r) {
//     alert("Точка лежит снаружи");
// } else if(radius < r) {
//     alert("Точка лежит внутри окружности");
// } else if(radius == r) {
//     alert("Точка лежит на окружности");
// }
// ----------------------
// Пользователь вводит пложительное число. Вывести все числа от 0 до числа. 
// var x = parseInt(prompt("Введите пложительное число"));
// var array = [];
// for(i = 0; i <= x; i++) {
//     array.push(i);
// }
// alert(array);

// Пользователь вводит два числа (любые). Вывести все числа от одного до второго.
// var x = parseInt(prompt("Введите первое число"));
// var y = parseInt(prompt("Введите второе число"));
// var array = [];
// var d = 0;
// for(i = x; i <= y ; i++) {
//             d = i;
//             array.push(d);
//     }
//     alert(array); 
// Пользователь вводит два числа ( первое < второго). Вывести сумму всех чисел между ними.
// var x = parseInt(prompt("Введите первое число"));
// var y = parseInt(prompt("Введите второе число"));
// var sum = 0;

// for(i = x; i <= y ; i++) {
//         sum = sum + i;
//     }
//     alert(sum); 

// Пользователь вводит два числа ( первое < второго). Вывести сумму всех чётных чисел между ними.
var x = parseInt(prompt("Введите первое число"));
var y = parseInt(prompt("Введите второе число"));
var sum = 0;

for(i = x; i <= y ; i++) {
       if (i % 2 == 0) {
        sum = sum + i;
       } 
    }
    alert(sum); 







