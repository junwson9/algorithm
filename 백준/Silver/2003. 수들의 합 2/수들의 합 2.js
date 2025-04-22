let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const lst = input[1].split(" ").map(Number);

let s = 0;
let e = 1;
let cnt = 0;

while (e <= N && s <= e) {
  let sm = 0;
  for (let i = s; i < e; i++) {
    sm += lst[i];
  }
  if (sm < M) {
    e += 1;
  } else if (sm > M) {
    s += 1;
  } else {
    cnt += 1;
    e += 1;
  }
}
console.log(cnt);