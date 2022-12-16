// 하... 설마 똑같은 코드인데 js로 하면 되는건 아니겠지;
const input = require("fs")
  .readFileSync("./dev/stdin", "utf8")
  .trim()
  .split("\n");

const N = Number(input[0]);

const pos = Array.from({ length: N }, () => 0);
let cnt = 0;

function validate(x, y) {
  for (let qy = 0; qy < y; qy++) {
    qx = pos[qy];
    if (qx === x || Math.abs(qy - y) === Math.abs(qx - x)) {
      return false;
    }
  }
  return true;
}

function recursive(y) {
  if (y === N) {
    cnt++;
    return;
  }

  for (let x = 0; x < N; x++) {
    pos[y] = x;
    if (validate(x, y)) {
      recursive(y + 1);
    }
  }
}

recursive(0);
console.log(cnt);
