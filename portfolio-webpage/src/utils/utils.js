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


export {
  getRangeOfNumbers,
  formatMonth
}