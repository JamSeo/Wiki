function solution(progresses, speeds) {
  let answer = [];

  let workingDays = progresses.map((progress, idx) => {
    return Math.ceil((100 - progress) / speeds[idx]);
  })

  let MaxDay = workingDays[0];
  let count = 0

  workingDays.forEach((workingDay) => {
    if (workingDay > MaxDay) {
      answer.push(count);
      MaxDay = workingDay;
      count = 0;
    }
    count++
  })
  answer.push(count)

  return answer;
}