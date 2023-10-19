function solution(n, computers) {
  let answer = 0;
  let visited = new Array(n).fill(false);

  computers.forEach((computer, i) => {
    // 이미 방문했으면 건너뛰기
    if (visited[i] === true) return;
    answer++;
    let queue = [i];

    // 탐색
    while (queue.length > 0) {
      let ci = queue.pop();
      visited[ci] = true;

      computers[ci].forEach((isLinked, j) => {
        if (visited[j] === true || !isLinked) return;
        queue.push(j);
      });
    }
  });

  return answer;
}
