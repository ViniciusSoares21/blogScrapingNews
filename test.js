const list = ['vinicius', 'Felps'];

const typeStr = JSON.stringify(list)
const typeList = JSON.parse(typeStr)

console.log(typeof typeStr)
console.log(typeof typeList);