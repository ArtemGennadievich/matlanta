// Скрипт "Спасибо за заказ"
let timer; // пока пустая переменная
let x =5; // стартовое значение обратного отсчета
countdown(); // вызов функции
function countdown(){  // функция обратного отсчета
  document.getElementById('rocket').innerHTML = x;
  x--; // уменьшаем число на единицу
  if (x<0){
    window.location.href = "/" // таймер остановится на нуле

  }
  else {
    timer = setTimeout(countdown, 1000);
  }
}
