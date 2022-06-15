const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num = Number(input[0]);
const stack = [];
const log = [];

for (let i = 1; i <= num; i += 1){
    const cmd = input[i].split(" ");

    switch (cmd[0]) {
        case 'push':
            stack.push(Number(cmd[1]));
            break;
        case 'pop':
            if (stack.length > 0){
                log.push(stack[stack.length - 1]);
                stack.pop();
            } else log.push(-1);
            break;
        case 'size':
            log.push(stack.length);
            break;
        case 'empty':
            if (stack.length > 0) log.push(0);
            else log.push(1);
            break;
        case 'top':
            if (stack.length > 0) log.push(stack[stack.length -1]);
            else log.push(-1);
            break;
    }
}
console.log(log.join("\n"));