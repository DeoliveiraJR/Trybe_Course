// Imagine que estamos exportando uma função, de modo que podemos utilizá-la para converter um valor em dólares para outro valor,neste caso em reais.

// O uso desse nosso módulo se daria da seguinte forma:
// index.js
// const convert = require('./brlValue');

// const usd = 10;
// const brl = convert(usd);

// console.log(brl) // 53.7

// index.js
// const brlValue = require('./brlValue');

// console.log(brlValue); // { brl: 5.37, usdToBrl: [Function: usdToBrl] }

// console.log(`Valor do dólar: ${brlValue.brl}`); // Valor do dólar: 5.37
// console.log(`10 dólares em reais: ${brlValue.usdToBrl(10)}`); // 10 dólares em reais: 53.7

// Como estamos lidando com um objeto, podemos utilizar object destructuring para transformar as propriedades do objeto importado em constantes no escopo global:
const { brl, usdToBrl } = require('./brlValue');

console.log(`Valor do dólar: ${brl}`); // Valor do dólar: 5.37
console.log(`10 dólares em reais: ${usdToBrl(10)}`); // 10 dólares em reais: 53.7