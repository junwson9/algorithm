let input = require("fs").readFileSync("dev/stdin").toString().trim();
const N = Number(input);
const v = Array(N + 1).fill(0);

function dfs(n, tmp) {
  if (n === N) {
    console.log(tmp.join(" "));
    return;
  }

  for (let i = 1; i < N + 1; i++) {
    if (v[i] === 0) {
      v[i] = 1;
      tmp.push(i);
      dfs(n + 1, tmp);
      tmp.pop();
      v[i] = 0;
    }
  }
}

dfs(0, []);
