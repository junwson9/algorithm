let input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
const lst = input.slice(1, N + 1).map((el) => el.split(" ").map(Number));
let answer = 0;

function dfs(n) {
  if (n > N) {
    return -123512351233624;
  }

  if (n === N) {
    return 0;
  }

  return Math.max(dfs(n + lst[n][0]) + lst[n][1], dfs(n + 1));
}

answer = dfs(0);
console.log(answer);
