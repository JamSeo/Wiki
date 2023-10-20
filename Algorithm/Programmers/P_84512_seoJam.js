function solution(word) {
  const AEIOU = ["A", "E", "I", "O", "U"];

  const arr1 = AEIOU;

  const arr2 = [];
  arr1.forEach((el) => {
    AEIOU.forEach((str) => arr2.push(el + str))
  })

  const arr3 = [];
  arr2.forEach((el) => {
    AEIOU.forEach((str) => arr3.push(el + str))
  })

  const arr4 = [];
  arr3.forEach((el) => {
    AEIOU.forEach((str) => arr4.push(el + str))
  })

  const arr5 = [];
  arr4.forEach((el) => {
    AEIOU.forEach((str) => arr5.push(el + str))
  })

  const dictionary = ['0', ...arr1, ...arr2, ...arr3, ...arr4, ...arr5].sort();

  for (let idx = 0; idx < dictionary.length; idx++) {
    if (word === dictionary[idx]) return idx
  }
}