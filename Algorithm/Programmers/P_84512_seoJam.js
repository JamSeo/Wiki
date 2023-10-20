// 조합을 만드는 함수
function generateCombinations(base) {
  const newCombinations = [];
  ["A", "E", "I", "O", "U"].forEach((char) => {
    newCombinations.push(base + char);
  });
  return newCombinations;
}

function solution(word) {
  const MAX_LENGTH = 5;
  let dictionary = ['0'];

  // 초기값 설정
  let currentWords = ["A", "E", "I", "O", "U"];

  // 최대 길이가 될 때까지 조합 생성
  for (let i = 0; i < MAX_LENGTH; i++) {
    dictionary = dictionary.concat(currentWords);
    let temp = [];
    currentWords.forEach((word) => {
      temp = temp.concat(generateCombinations(word));
    });
    currentWords = temp;
  }

  // word의 위치 찾기
  return dictionary.sort().indexOf(word)
}