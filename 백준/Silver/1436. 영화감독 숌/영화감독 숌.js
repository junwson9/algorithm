let input = require("fs").readFileSync("dev/stdin").toString().trim();
input = Number(input);

const num = "666";
let cnt = 0;
let i = 666;
while (true) {
  if (cnt === input) {
    break;
  }
  if (String(i).includes(num)) {
    cnt += 1;
  }
  i++;
}

console.log(i - 1);
