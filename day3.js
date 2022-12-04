const { readFileSync } = require('fs');

fileName = "examples/example3.txt"

const inputFile = readFileSync(fileName, 'utf-8')

const rucksacks = inputFile.split('\n')

// function getCommon(rucksack){
//     rucksack.map
// }

sampleString = "jdsfljhdfslUHJIdjfdJ"


console.log(sampleString)

const firstHalf = sampleString.slice(0, sampleString.length / 2).split('')
const secondHalf = sampleString.slice(sampleString.length / 2, sampleString.length).split('')



const test = firstHalf.filter(char=>secondHalf.includes(char))

console.log(test)