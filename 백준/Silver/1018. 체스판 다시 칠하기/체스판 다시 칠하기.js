let input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number);

let board = input.slice(1, N + 1).map((row) => row.trim().split(""));
let answer = [];

for (r = 0; r < N - 7; r++) {
  for (c = 0; c < M - 7; c++) {
    let w_cnt = 0;
    let b_cnt = 0;
    for (i = r; i < r + 8; i++) {
      for (j = c; j < c + 8; j++) {
        if ((i + j) % 2 === 0) {
          if (board[i][j] !== "W") {
            w_cnt += 1;
          } else {
            b_cnt += 1;
          }
        } else {
          if (board[i][j] !== "B") {
            w_cnt += 1;
          } else {
            b_cnt += 1;
          }
        }
      }
    }
    answer.push(w_cnt);
    answer.push(b_cnt);
  }
}

console.log(Math.min(...answer));
