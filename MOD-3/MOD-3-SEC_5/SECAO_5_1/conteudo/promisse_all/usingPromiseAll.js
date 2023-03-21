// usingPromiseAll.js

const fs = require('fs').promises;

const files = [
  'file1.txt',
  'file2.txt',
  'file3.txt',
]

async function main() {
  try {
    const promises = files.map(async (file, index) => {
      const contentFile = await fs.readFile(file, 'utf8');
      console.log(`File ${index + 1}: ${contentFile}`)
    })
    await Promise.all(promises);
    console.log(`That's all folks!`);
  } catch (err) {
    console.error(`Erro ao ler o arquivo: ${err.message}`);
  }
}

main()

async function getFilesSizeSum() {
  try {
    let filesSizeSum = 0
    await Promise.all(files.map(async (file) => {
      contentFile = await fs.readFile(file);
      filesSizeSum = filesSizeSum + contentFile.byteLength;
    }));
    result = `Lidos 3 arquivos totalizando ${filesSizeSum} bytes`;
    return console.log(result);
  } catch (err) {
    console.error(`Erro ao ler o arquivo: ${err.message}`);
  }
}

getFilesSizeSum()

// Também podemos encadear promises, utilizando o .then e escrever a função acima da seguinte forma:

Promise.all([
  fs.readFile('file1.txt'),
  fs.readFile('file2.txt'),
  fs.readFile('file3.txt'),
])
  .then(([file1, file2, file3]) => {
    const fileSizeSum = file1.byteLength + file2.byteLength + file3.byteLength;
    console.log(`Lidos 3 arquivos totalizando ${fileSizeSum} bytes`);
  })
  .catch((err) => {
    console.error(`Erro ao ler arquivos: ${err.message}`);
  });

// Para fixar
// Com o módulo fs, crie uma função que lê e escreve vários arquivos ao mesmo tempo.
// Utilize o Promise.all para manipular vários arquivos ao mesmo tempo.
// Dado o seguinte array de strings: ['Finalmente', 'estou', 'usando', 'Promise.all', '!!!'], faça com que sua função crie um arquivo contendo cada string, sendo o nome de cada arquivo igual a file<index + 1>.txt. Por exemplo, para a string “Finalmente”, o nome do arquivo é file1.txt.
// Programe sua função para que ela faça a leitura de todos os arquivos criados no item anterior, armazene essa informação e escreva em um arquivo chamado fileAll.txt.
// O conteúdo do arquivo fileAll.txt deverá ser Finalmente estou usando Promise.all !!!.
async function arrayToFile() {

    const strings = ['Finalmente', 'estou', 'usando', 'Promise.all', '!!!'];
    const fileNames = [
      'file1.txt',
      'file2.txt',
      'file3.txt',
      'file4.txt',
      'file5.txt',
    ];

    const createFilesPromises = strings
      .map((string, index) => fs.writeFile(`./file${index + 1}.txt`, string));

    await Promise.all(createFilesPromises);

    // aqui usamos a mesma estratégia
    // criamos uma promise de leitura para cada item no array `fileNames`
    const readFilesPromises = fileNames
      .map((fileName) => fs.readFile(fileName, 'utf-8'));

    // e aqui esperamos que todas as leituras sejam resolvidas
    const fileContents = await Promise.all(readFilesPromises);

    const newFileContent = fileContents.join(' ');

    await fs.writeFile('./fileAll.txt', newFileContent);
}

arrayToFile() // caso queira esperar a resolução, use o `await` ou `.then`