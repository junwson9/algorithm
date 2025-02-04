let input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
const [N, K] = input[0].split(" ").map(Number);
const lst = input[1].split(" ").map(Number);
lst.unshift(0);

let prefix = Array(N + 1).fill(0);

for (let i = 1; i < N + 1; i++) {
  prefix[i] = prefix[i - 1] + lst[i];
}
let answer = -Infinity;
for (let i = K; i < prefix.length; i++) {
  if (prefix[i] - prefix[i - K] > answer) {
    answer = prefix[i] - prefix[i - K];
  }
}
console.log(answer);
