function solution(sizes) {
  let minw = 0;
  let minh = 0;

  sizes.forEach(([len1, len2]) => {
    let w = Math.max(len1, len2);
    let h = Math.min(len1, len2);

    minw = Math.max(minw, w);
    minh = Math.max(minh, h);
  })

  return minw * minh;
}