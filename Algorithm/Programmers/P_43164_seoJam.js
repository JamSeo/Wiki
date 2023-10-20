function solution(tickets) {
  let answer = [];
  let path = [];
  let isVisited = new Array(tickets.length).fill(0);
  tickets.sort();

  const dfs = (current, count) => {
    path.push(current);

    // 경로가 완성된 경우
    if (count === tickets.length) {
      answer = path;
      console.log(answer, path);
      return true;
    }

    for (let idx = 0; idx < tickets.length; idx++) {
      let [depart, arrival] = tickets[idx];

      if (!isVisited[idx] && current === depart) {
        isVisited[idx] = 1;
        if (dfs(arrival, count + 1)) return true;
        isVisited[idx] = 0;
      }
    }
    path.pop();
    return false;
  };

  dfs("ICN", 0);
  console.log(answer);
  return answer;
}
