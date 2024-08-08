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
var n = +prompt("Введите число");
for (i=1; i<=100; i++) {
    if (i % n == 0) { 
        console.log(i);
    }
}