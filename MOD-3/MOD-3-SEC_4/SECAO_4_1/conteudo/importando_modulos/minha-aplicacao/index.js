// Quando queremos importar um módulo local, precisamos passar para o require o caminho do módulo, seguindo a mesma assinatura.

// Além de importarmos um arquivo como módulo, podemos importar uma pasta. Isso é útil, pois muitas vezes um módulo está dividido em vários arquivos, porém, desejamos importar todas as suas funcionalidades de uma única vez. Nesse caso, a pasta precisa conter um arquivo chamado index.js, o qual importa cada um dos arquivos do módulo e os exporta da forma mais conveniente.

// minha-aplicacao/index.js
const meuModulo = require('../meuModulo');

console.log(meuModulo); // { funcionalidade1: [Function: funcionalidade1], funcionalidade2: [Function: funcionalidade2] }

meuModulo.funcionalidade1();