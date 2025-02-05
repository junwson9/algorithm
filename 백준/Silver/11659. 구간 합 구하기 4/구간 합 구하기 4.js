let input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const lst = input[1].split(" ").map(Number);
const arr = input.slice(2, M + 2).map((el) => el.split(" ").map(Number));

lst.unshift(0);

const prefix = Array(N + 1).fill(0);

for (let i = 1; i < lst.length; i++) {
  prefix[i] = prefix[i - 1] + lst[i];
}

for (let i = 0; i < arr.length; i++) {
  console.log(prefix[arr[i][1]] - prefix[arr[i][0] - 1]);
}
