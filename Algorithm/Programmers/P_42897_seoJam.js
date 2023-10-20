function solution(money) {
  const N = money.length;  // 집 개수

  // 첫 번째 집부터 방문하는 경우
  const dp1 = new Array(N).fill(0);
  dp1[0] = dp1[1] = money[0];
  for (let i = 2; i < N; i++) {
    dp1[i] = Math.max(dp1[i - 1], money[i] + dp1[i - 2]);
  }

  // 두 번째 집부터 방문하는 경우
  const dp2 = new Array(N).fill(0);
  dp2[0] = 0, dp2[1] = money[1];
  for (let i = 2; i < N; i++) {
    dp2[i] = Math.max(dp2[i - 1], money[i] + dp2[i - 2]);
  }

  return Math.max(dp1[N - 2], dp2[N - 1]);
}