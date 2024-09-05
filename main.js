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
// var x = parseInt(prompt("Введите первое число"));
// var y = parseInt(prompt("Введите второе число"));
// var sum = 0;

// for(i = x; i <= y ; i++) {
//        if (i % 2 == 0) {
//         sum = sum + i;
//        } 
//     }
//     alert(sum); 
//---------------------------------------------------
// var answer;
// line = [];
// for (i = 2; i < 10; i++) {
//         for (j = 1; j < 11; j++) {
//                 answer = i * j;
//                 line.push(answer);
               
//         }
//         document.write(line);
//         document.write('<br>');
//         line=[];
// }
//---------------------------------------------------

// let a = [465, 564, 98797, 13, 324, 56742, 648, 243333374357,5476566,56465];
// let max = 0;
// for(i = 0; i < a.length; i++) {
//         if (a[i] > max) {
//                 max = a[i];
//         }
// }alert(max);
//---------------------------------------------------
// let a = [465, 564, 98797, 13, 324, 56742, 648, 243333374357,5476566,56465];
// for(i = 0; i < a.length; i++) {
//     for(k = i; k < i; k++) {
//         if(a[i] > a[k]) {
//             a[i] = a[k];
//         }
//     }
// }
// alert[a];
//---------------------------------------------------

// if (confirm("загадай целое число от 0 до 100")) {
//     var arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100];
//     var N;
//     for(i = 0; i <= 100; i++) {
//         N  =  arr[Math.floor(arr.length / 2)];
//         var symbol = prompt("Ваше число > " + N + " или < " + N + " или = " + N + " ?");
//         if(symbol == ">") {
//             for(j = 1; j < arr.length; j++) {
//                 arr[j-1] = arr[Math.floor(arr.length / 2)+j];
//                 arr[j] = arr[j-1];
//             }
//             arr.length = Math.floor(arr.length / 2);
//         }  else if(symbol == "<") {
//             arr.length = Math.floor(arr.length / 2);
//         } else {
//             alert("Я угодал!!!=)")
//             break;
//         }
//         if(arr.length == 1) {
//             N = arr;
//             var symbol = prompt("Ваше число = " + N + " ?");
//             if(symbol == "=") {
//                 alert("Я угодал!!!=)")
//                 break;
//             }
//         }
//     } 
// }
//----------------------------------------------------
// var number = prompt("Введите число").split("");
// var step = parseInt(prompt("Введите на сколько сдвинуть число число"));
// for (var i = 0; i < step; i++) {
//   var arr = number[0];
//   for (var j = 1; j < number.length; j++) {
//     number[j - 1] = number[j];
//     number[j] = number[j + 1];
//   }
//   number[number.length - 1] = arr;
// }
// alert(number.join(""));

//----------------------------------------------------
// var x = parseInt(prompt("Введите любое число"));
// function minus(x) {
// if (x < 0) {
//     return -1
// } return 1
// }

// alert(minus(x));
//----------------------------------------------------
// function bolmen(a, b) {
// if (a < b) {
//     return a + "<" + b;
// } else if (a > b) {
//     return a + ">" + b;
// } else {
//     return a + "=" + b;
// }
// }
// let number = bolmen(+prompt("Введите первое число"), +prompt("Введите второе число"))
// alert(number);
//----------------------------------------------------
// function stepen(a, s) {
//     sum = 1;
//     for (let i = 1; i <= s; i++) {
//         sum *= a;
//     }
//     return sum;
// }
// let number = stepen(+prompt("Введите целое число"), +prompt("Введите в какую степень возвести"))
// alert(number);
//----------------------------------------------------
// function calc(x, symbol, y) {
//     let answer;
//     if(symbol == "/") {
//         if(y == 0) {
//             return "На ноль делить нельзя"
//         }
//         answer =  x / y
//     } else if(symbol == "*") {
//     answer =  x * y
//     } else if(symbol == "-") {
//     answer =  x - y
//     } else if(symbol == "+") {
//     answer =  x + y
//     }
//     return answer;
// }
// alert(calc((parseInt(prompt("Введите первое число"))), prompt("Введите операцию '/' или '*' или '-' или '+'"), parseInt(prompt("Введите второе число"))));
//----------------------------------------------------
// function summa(a, b, c, d, e) {
//     if (isNaN(a)) {
//         a = 0;
//     } 
//     if(isNaN(b)) {
//         b = 0;
//     }
//     if(isNaN(c)) {
//         c = 0;
//     } 
//     if(isNaN(d)) {
//         d = 0;
//     }
//     if(isNaN(e)) {
//         e = 0;
//     } 
//     let answer = a + b + c + d + e;
//     return answer;
// }
// alert(summa((parseInt(prompt("Введите первое число"))), (parseInt(prompt("Введите второе число"))), (parseInt(prompt("Введите третье число"))), (parseInt(prompt("Введите четвертое число"))), (parseInt(prompt("Введите пятое число")))));

//----------------------------------------------------
// function sum() {
//     arr = 0;
//     for(i = 0; i < arguments.length; i++) {
//         arr += arguments[i];
//     }
// return arr;
// }
// alert(sum(5,5));
//----------------------------------------------------
// function min() {
//         minimum = arguments[0];
//         for(i = 0; i < arguments.length; i++) {
//             if(arguments[i] < minimum) {
//                 minimum = arguments[i];
//             }
//         }
//     return minimum;
//     }
//     alert(min(5,5,-5,-100,69,0,1));
//----------------------------------------------------
// function stroka() {
//     s = '';
//     for(i = 0; i < arguments.length; i++) {
//         s += arguments[i] + ' ';
//     }
//     return s;
// }
// alert(stroka("Привет", "Олег", "как", "дела","?"))
//----------------------------------------------------
// function massivData() {
//     mData  = [];
//     for(i = 0; i < arguments.length; i++) {
//         if(typeof arguments[i] == "number") {
//             mData.push(arguments[i]);
//         }
//     }
//     return mData;
// }
// alert(massivData(NaN, undefined, false, true, 5, 3, Infinity));
// alert(typeof -Infinity);
//----------------------------------------------------
// function stroka(a, b) {
//     if (a.length > b.length) {
//         return 1;
//     } else if(a.length < b.length) {
//         return -1;
//     } else {
//         return "Длина строк одинакова";
//     }
// }
// alert(stroka(prompt("введите первую строку"), prompt("введите вторую строку")));
//----------------------------------------------------

// function stroka(a) {
//     return a[0].toUpperCase() + a.slice(1);
// }
// alert(stroka(prompt("введите cтроку")));
//----------------------------------------------------
// function stroka(str) {
//     g = "уеаоэяиюы"; 
//     let counter = 0;
//     for(let i = 0; i < str.length; i++) {
//         if(g.includes(str[i])) {
//             counter += i;
//         }
//     }
// }
// alert(stroka(prompt("Введите строку")));
//----------------------------------------------------
// function chek_spam(str) {
//     const spam_words = ['100 безплатно завтра','увелечение продаж', 'только сегодня', 'не удаляйте'];

//     let lower_case_str = str.toLowerCase();
//     for(let i = 0; i < lower_case_str; i++) {
//         if (lower_case_str.includes(spam_words[i])) {
//             return true;
//         }
//     }
//     return false;
// }   
// console.log(chek_spam('100 безплатно завтра'));
// console.log(chek_spam('завтра'));
// console.log(chek_spam('только сегодня'));
//----------------------------------------------------
// const student = {
//     name: 'Oleg',
//     surname: 'Petrov',
//     age: 20,
//     is_student: true,
// }
// console.log(student);
// console.log(student.name);
// delete student.age;
// console.log(student);

// for (let j in student) {
//     console.log(j);
//     console.log(student[j]);
// }
//----------------------------------------------------
// const car = {
//     make: 'AutoVAZ',
//     model: 'Lada Vesta',
//     year: 2018,
// }
// // console.log(car.make + car.model + car.year);
// console.log(`Make: ${car.make}, Model: ${car.model}, Make: ${car.year}`);
//----------------------------------------------------
// const person = {
//     name: "Oleg",
//     age: 40,
// }
// person.gender = "Man";
// person.age = 21;
// console.log(person);
//----------------------------------------------------
// const book = {
//     title: "Мастер и Маргарита",
//     author: "Михаил Булгаков",
//     year: 1940,
// }
// delete book.year;
// console.log(book);
//----------------------------------------------------
// const user = {
//     username: "Terminator",
//     email: "arni@gmail.com",
//     password: 4242,
// }
// for(let i in user) {
//     console.log(i + " - " + user[i]);
// }
//----------------------------------------------------
// const company = {
//     address: {
//         street: "Lenina",
//         city: "Ryazan",
//         zipCode: 234123,
//     }
// }
// console.log(`Street: ${company.address.street}, City: ${company.address.city}, Zip Code: ${company.address.zipCode},`);
//----------------------------------------------------
// const students = [
//     {
//         name: "Petrov",
//         bal: 5,
//     },
//     {
//         name: "Ivanov",
//         bal: 5,
//     },
//     {
//         name: "Frolov",
//         bal: 5,
//     },
//     {
//         name: "Sidorov",
//         bal: 5,
//     },
//     {
//         name: "Masunov",
//         bal: 5,
//     },
//     {
//         name: "Hrenov",
//         bal: 5,
//     },
// ]
// function sred_bal(a) {
//     let summ = 0;
//     let summ_sr = 0;
//     for (let i = 0; i < a.length; i++) {
//         summ += a[i].bal;
//     }
//     summ_sr = summ / a.length;
//     return summ_sr;
// }
// console.log(sred_bal(students));
//----------------------------------------------------
// const settings = {
//     volume: 5,
//     date: 24,
//     hren: 2,
// }
// function blablabla(a, b) {
//     for(let key in a) {
//         if (typeof a[key] === 'number') {
//             a[key] += b
//         }
//     }
//     return a;
// }
// console.log(blablabla(settings, 1));
//----------------------------------------------------
// const car_settings = {
//     make: "LADA",
//     model: "Vesta",
//     age: 2018,
//     speed: 70,
// }

// function info_car(a) {
//     console.log(`Make: ${car_settings.make}, Model: ${car_settings.model}, Age: ${car_settings.age}, Speed: ${car_settings.speed}`); 
// }

// info_car(car_settings)

// function time(obj, s) {
//         let time = s / obj.speed;
//         let delay = Math.floor(time / 4);
//         let total_time = time + delay;

//         return total_time;
// }
// console.log(time(car_settings, 1050));




//--------------------- OOP--------------------------------------------------------



class Human {
        constructor(name, surname, age) {
                this.name = name;
                this.surname = surname;
                this.age = age;
        }
        display_info() {
            console.log(`Name: ${this.name}, Surname: ${this.surname}, Age: ${this.age}`);
        }
}
const oleg = new Human('Oleg', 'Ivanov', '40');
const alex = new Human('Alex', 'Petrov', '35');

oleg.display_info();
alex.display_info();