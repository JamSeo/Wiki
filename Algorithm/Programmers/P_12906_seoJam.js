function solution(arr) {
  const answer = [];

  arr.forEach((num) => {
    if (num === answer?.[answer.length - 1]) return;
    answer.push(num);
  })

  return answer;
}