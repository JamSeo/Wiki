function solution(triangle) {
  const N = triangle[triangle.length - 1].length;
  const MAX_VALUE = Number.POSITIVE_INFINITY;

  // dp 만들기
  const dp = [];
  for (let i = 0; i < N; i++) {
    let row = new Array(i + 1).fill(MAX_VALUE);
    dp.push(row);
  }

  // 시작점 저장
  dp[0][0] = triangle[0][0];

  // dp 채우기
  for (let i = 1; i < N; i++) {
    for (let j = 0; j < i + 1; j++) {
      p1 = dp[i - 1]?.[j] ?? 0;
      p2 = dp[i - 1]?.[j - 1] ?? 0;
      dp[i][j] = Math.max(triangle[i][j] + p1, triangle[i][j] + p2);
    }
  }

  return Math.max(...dp[dp.length - 1]);
}