// Exemplo fazendo o teste de model na mão

const { expect } = require('chai');
const { Book } = require('../../models');

describe('O model de Book', function () {
  it('possui a propriedade "title"', function () {
    const book = new Book();
    expect(book).to.have.property('title');
  });

  it('possui a propriedade "author"', function () {
    const book = new Book();
    expect(book).to.have.property('author');
  });

  it('possui a propriedade "pageQuantity"', function () {
    const book = new Book();
    expect(book).to.have.property('pageQuantity');
  });

  it('possui a propriedade "publisher"', function () {
    const book = new Book();
    expect(book).to.have.property('publisher');
  });
});

// Exemplo de teste do model usando o sequelize-test-helpers:
// const { expect } = require('chai');
// const { Book } = require('../../models');

// describe('O model de Book', function () {
//   it('possui a propriedade "title"', function () {
//     const book = new Book();
//     expect(book).to.have.property('title');
//   });

//   it('possui a propriedade "author"', function () {
//     const book = new Book();
//     expect(book).to.have.property('author');
//   });

//   it('possui a propriedade "pageQuantity"', function () {
//     const book = new Book();
//     expect(book).to.have.property('pageQuantity');
//   });

//   it('possui a propriedade "publisher"', function () {
//     const book = new Book();
//     expect(book).to.have.property('publisher');
//   });
// });
