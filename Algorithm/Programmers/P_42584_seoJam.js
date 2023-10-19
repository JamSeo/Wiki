function solution(prices) {
  let answer = new Array(prices.length).fill(0);
  let stack = new Array();

  prices.forEach((price, idx) => {
    // stack에 있는 값들 중에 input 값보다 큰 값들은 pop해줌
    while (stack !== null && price < prices[stack[stack.length - 1]]) {
      let bigIdx = stack.pop();
      answer[bigIdx] = idx - bigIdx;
    }
    // input 값을 stack에 넣음
    stack.push(idx);
  })

  // stack에 가장 마지막 값 저장
  const lastIdx = stack[stack.length - 1];
  // stack에 남아있는 값들 털어내기
  stack.forEach((pricesIdx) => {
    answer[pricesIdx] = lastIdx - pricesIdx;
  })

  return answer;
}