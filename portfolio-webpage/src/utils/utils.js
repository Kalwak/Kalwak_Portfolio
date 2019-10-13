function getRangeOfNumbers(min, limit) {
  let numbers = [];
  let number = min;
  for (; number <= limit; number++) {
    numbers.push(number);
  }

  return numbers;
}

function formatMonth(month) {
  let months = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"];
  if (typeof month !== 'string' || !month.length) return false;
  month = months.indexOf(month) + 1;
  month = month.toString().length === 1 ? '0' + month : month;
  return month;
}

function formatPostDate(date) { // format should be -> yy-mm-dd
  const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
  const datePieces = date.split('-');
  let [year, month, day] = datePieces;

  month = month.split('');
  let monthIndex = Number((month[0] === '0' ? month[1] : month.join(''))) - 1;
  month = months[monthIndex];

  day = day.split('');
  day = day[0] === '0' ? day[1] : day;
  day = day.join('');

  let finalDate = `Publicado el ${day} de ${month} del ${year}`;
  return finalDate
}

export {
  getRangeOfNumbers,
  formatMonth,
  formatPostDate,
}