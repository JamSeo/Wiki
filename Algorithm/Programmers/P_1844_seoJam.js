function solution(maps) {
  const MAX_NUM = Number.POSITIVE_INFINITY
  const DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  const N = maps.length;
  const M = maps[0].length;

  let stack = [[0, 0]];
  let isVisited = new Array(N).fill([]);
  isVisited.forEach((_, idx) => {
    isVisited[idx] = new Array(M).fill(MAX_NUM);
  })
  isVisited[0][0] = 1;

  // 백트래킹
  if (!maps[N - 1][M - 2] && !maps[N - 2][M - 1] && !maps[N - 2][M - 2]) return -1;

  while (stack.length > 0) {
    let [ci, cj] = stack.shift();
    let cvalue = isVisited[ci][cj];

    for (let [di, dj] of DIRECTION) {
      let [ni, nj] = [di + ci, dj + cj];

      // 벗어난 경우
      if (ni < 0 || nj < 0 || N <= ni || M <= nj) continue;

      // 벽인 경우
      if (maps[ni][nj] === 0) continue;

      // 지나온 경로에 최솟값 저장
      if (isVisited[ni][nj] > cvalue + 1) {
        isVisited[ni][nj] = cvalue + 1;
        stack.push([ni, nj]);
      }
    }
  }

  return isVisited[N - 1][M - 1] === MAX_NUM ? -1 : isVisited[N - 1][M - 1];
}