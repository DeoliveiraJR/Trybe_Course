// src/models/user.model.js
const UserModel = (sequelize, DataTypes) => {
 const User = sequelize.define('User', {
   fullName: DataTypes.STRING,
   email: DataTypes.STRING,
 });
  (async () => {
    await sequelize.sync({ force: true });
    // As funções vão aqui
    const sara = User.build({
        fullName: 'Sara Silva Santos',
        email: 'sara.ss@trybe.com',
        // aqui inserimos o datatype da coluna criada
       phoneNum: DataTypes.STRING,
    });

    await sara.save();

    console.log(sara instanceof User); // true
    console.log(sara.fullName); // "Sara Silva Santos"
    console.log('Pessoa salva no banco de dados!');

    // Criando com create
    // Uma forma mais simples de criar uma instância de um model e salvá-la no banco de dados é usando o método create, que combina o build e o save em uma única função:

    // const sara = await User.create({
    //     fullName: 'Sara Silva Santos',
    //     email: 'sara.ss@trybe.com',
    // });

    // console.log(sara instanceof User); // true
    // console.log(sara.name); // "Sara Silva Santos"

    // Modificando informações no banco de dados
    // Quando trocamos informações de um model, precisamos salvar essas alterações no banco de dados. Para isso, podemos usar o método save:

    // const sara = await User.create({
    //     fullName: 'Sara Silva Santos',
    //     email: 'sara.ss@trybe.com',
    // });

    // console.log(sara.fullName); // "Sara Silva Santos"

    // sara.fullName = "Jane Doe";

    // O nome ainda está "Sara Silva Santos" no banco de dados!

    // await sara.save();

    // Agora o nome foi atualizado para "Jane Doe" no banco de dados!

    // Também é possível atualizar diversos campos de uma vez usando o método set:
    const lucas = await User.create({
        fullName: 'Lucas Silva Santos',
        email: 'lucas.ss@trybe.com',
    });

    lucas.set({
    fullName: "Pedro Silva Santos",
    email: "pedro.ss@trybe.com"
    });

    // O nome ainda está "Lucas Silva Santos" no banco de dados!

    await lucas.save();

    // Agora o nome foi atualizado para "Pedro Silva Santos", e o email para pedro.ss@trybe.com no banco de dados!

})();
 return User;
};

module.exports = UserModel;
