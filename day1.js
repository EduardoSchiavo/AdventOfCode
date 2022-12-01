const {readFileSync, promises: fsPromises} = require('fs');

filename="examples/example1.txt"

const contents = readFileSync(filename, 'utf-8').split("\n\n");

let load_per_elf = []

contents.forEach((item) => load_per_elf.push(item.split('\n').map(Number).reduce((a,b)=>a+b)))

// P1
console.log("Part one:", Math.max(...load_per_elf))

// P2

console.log(load_per_elf.sort((a,b)=>b-a).slice(0,3).reduce((a,b)=>a+b))