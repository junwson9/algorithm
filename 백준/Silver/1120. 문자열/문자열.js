let input = require("fs").readFileSync("dev/stdin").toString().trim().split(" ");
const [A, B] = input;
const arr1 = [...A];
const arr2 = [...B];

diff = arr2.length - arr1.length;
if (!diff) {
  let cnt = 0;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      cnt += 1;
    }
  }
  console.log(cnt);
} else {
  let answer = 99999999999999;
  for (let i = 0; i < diff + 1; i++) {
    let cnt = 0;
    for (let j = 0; j < arr1.length; j++) {
      if (arr2[i + j] !== arr1[j]) {
        cnt += 1;
      }
    }
    answer = Math.min(answer, cnt);
  }
  console.log(answer);
}
