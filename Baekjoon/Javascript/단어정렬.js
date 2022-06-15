const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
input.shift();

sorted_lst = new Set(input);
sorted_lst = [...sorted_lst];

sorted_lst = sorted_lst.sort(function (a, b){
    if (a.length > b.length) return 1;
    if (a.length < b.length) return -1;
    if (a > b) return 1;
    if (a < b) return -1;
});

sorted_lst.map((ele) => console.log(ele));