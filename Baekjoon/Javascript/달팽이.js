const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(e1 => +e1)

let up = input[0];
let down = input[1];
let len = input[2];

let day = Math.ceil((len - down) / (up - down));
console.log(day)