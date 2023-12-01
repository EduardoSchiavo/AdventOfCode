const {readFileSync} = require('fs');

fileName="examples/example1.txt"

const inputFile = readFileSync(fileName, 'utf-8')

const loadPerElf = inputFile.split("\n\n").map((item) => (item.split('\n').map(Number).reduce((a,b)=>a+b)));

// P1
console.log("Part one:", Math.max(...loadPerElf));

// P2
console.log("Part two:",loadPerElf.sort((a,b)=>b-a).slice(0,3).reduce((a,b)=>a+b));