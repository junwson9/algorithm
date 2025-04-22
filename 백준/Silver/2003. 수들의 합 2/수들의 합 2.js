let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const lst = input[1].split(" ").map(Number);

let s = 0;
let e = 0;
let sm = 0;
let cnt = 0;

while (e<= N) {
  if (sm < M) {
    sm += lst[e++];
  } else if (sm > M) {
    sm -= lst[s++];
  } else {
    cnt++;
    sm -= lst[s++];
  }
}
console.log(cnt);
