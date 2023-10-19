function solution(fees, records) {
  let parkingTimes = {};
  const LAST_TIME = 23 * 60 + 59;

  records.forEach((record) => {
    const [time, carNum, carGoing] = record.split(" ");

    // 시간 parsing
    const [hour, min] = time.split(":").map(Number);
    let parsedTime = hour * 60 + min;

    // 처음 입차했을 때
    if (parkingTimes[carNum] === undefined) {
      parkingTimes[carNum] = 0;
    }

    // 누적 주차 시간 계산
    if (carGoing === "IN") {
      parkingTimes[carNum] -= parsedTime;
    } else {
      parkingTimes[carNum] += parsedTime;
    }
  });

  // 마지막 입차만 기록되고 출차 기록이 없는 경우 처리
  for (let carNum in parkingTimes) {
    if (parkingTimes[carNum] <= 0) {
      parkingTimes[carNum] += LAST_TIME;
    }
  }

  // parkingTimes를 차 번호 기준으로 오름차순 정렬
  const sortedCarNums = Object.keys(parkingTimes).sort();

  // answer 구하기
  return Object.values(sortedCarNums).map((carNum) => {
    let parkingTime = parkingTimes[carNum];
    let overTime = Math.max(parkingTime - fees[0], 0);
    return fees[1] + Math.ceil(overTime / fees[2]) * fees[3];
  });
}
