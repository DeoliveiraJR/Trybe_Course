/* type Character = any;

const characters: any = [
  {
    nickname: 'xKillerx',
    class: 'warrior',
    stats: { agi: 50, str: 100, int: 25, hp: 1000, mp: 300 },
    createdAt: new Date('2003-10-1')
  },                            
  {
    nickname: 'jainaProud',
    class: 'mage',
    stats: { agi: 80, str: 40, int: 150, hp: 630, mp: 1100 },
    createdAt: new Date('2003-10-2')
  },
  {
    nickname: 'catIn',
    class: 'hunter',
    stats: { agi: 150, str: 90, int: 80, hp: 800, mp: 600 },
    createdAt: new Date('2003-10-15')
  },
]

function printCharacter(character: any, index: number) {
  const { nickname, class: cls, createdAt } = character;

  console.log(`\n\n===== Character: ${index + 1} ========`);
  console.log(`nickname: ${nickname}
class: ${cls}
createdAt: ${createdAt}`);
}

characters.forEach(printCharacter);  */

// ==============================-----------------SOLUÇÃO:
// -------------------------------------------------------

/* type Character = {
    nickname: string;
    class: string;
    stats: { agi: number, str: number, int: number, hp: number, mp: number };
    createdAt: Date;
  };
  
  const characters: Character[] = [
    {
      nickname: 'xKillerx',
      class: 'warrior',
      stats: { agi: 50, str: 100, int: 25, hp: 1000, mp: 300 },
      createdAt: new Date('2003-10-1')
    },
    {
      nickname: 'jainaProud',
      class: 'mage',
      stats: { agi: 80, str: 40, int: 150, hp: 630, mp: 1100 },
      createdAt: new Date('2003-10-2')
    },
    {
      nickname: 'catIn',
      class: 'hunter',
      stats: { agi: 150, str: 90, int: 80, hp: 800, mp: 600 },
      createdAt: new Date('2003-10-15')
    },
  ]
  
  function printCharacter(character: Character, index: number) {
    const { nickname, class: cls, createdAt } = character;
  
    console.log(`\n\n===== Character: ${index + 1} ========`);
    console.log(`nickname: ${nickname}
  class: ${cls}
  createdAt: ${createdAt}`);
  }
  
  characters.forEach(printCharacter); */

  // ./index.ts

import readline from "readline-sync"; // importamos o pacote readline-sync

// criamos um array de objetos com o nome do script e o caminho do script a ser executado
const scripts = [
    { name: "Converter comprimento", script: "./length" },
    { name: "Converter massa", script: "./mass" },
    { name: "Converter capacidade", script: "./capacity" },
    { name: "Converter área", script: "./area" },
    { name: "Converter volume", script: "./volume" }
];

// criamos um novo array somente com os nomes dos scripts
const scriptNames = scripts.map(item => item.name);

// pedimos à pessoa usuária para escolher um dos scripts de conversão
const choice = readline.keyInSelect(scriptNames, "Escolha um número para executar o script de conversão de unidade");

require(scripts[choice].script); // executamos o script escolhido usando o require