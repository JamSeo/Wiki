function solution(str) {
  const stack = [];

  for (const el of str) {
    // 종료조건1: 괄호 짝이 맞지 않는 경우
    if (stack.length === 0 && el === ")") return false;

    if (el === "(") stack.push(el);
    else stack.pop();
  }

  // 종료조건2: 괄호가 닫히지 않은 경우
  if (stack.length > 0) return false;

  return true;
}