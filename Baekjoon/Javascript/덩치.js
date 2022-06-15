const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
    [n, ...person] = input;
    let result = [];

    for (let i = 0; i < n; i += 1){
        let rank = 0;
        for (let j = 0; j < n; j += 1){
            if (i === j) continue;
            [weight1, tall1] = person[i].split(' ');
            [weight2, tall2] = person[j].split(' ');

            if (Number(weight1) < Number(weight2) && Number(tall1) < Number(tall2)) rank += 1;
        }
        result.push(rank + 1);
    }
    return result.join(' ');
}

console.log(solution(input));