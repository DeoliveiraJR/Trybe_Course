// src/migrations/[timestamp]-create-user.js

// 'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
       await queryInterface.createTable('Users', {
         id: {
           allowNull: false,
           autoIncrement: true,
           primaryKey: true,
           type: Sequelize.INTEGER
         },
         fullName: {
           type: Sequelize.STRING
         },
         email: {
           type: Sequelize.STRING
         },
         createdAt: {
           allowNull: false,
           type: Sequelize.DATE
         },
         updatedAt: {
           allowNull: false,
           type: Sequelize.DATE
         }
       });
  },

  down: async (queryInterface, Sequelize) => {
          await queryInterface.dropTable('Users');
  }
};