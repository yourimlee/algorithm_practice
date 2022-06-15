let input = require('fs').readFileSync('/dev/stdin');

let count = 0;
while (true) {
    if (input % 5 === 0){
        console.log(input / 5 + count);
        break;
    }
    if (input < 0) {
        console.log(-1);
        break;
    }
    count++;
    input -= 3;
}