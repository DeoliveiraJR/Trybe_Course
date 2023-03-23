// src/config/config.js

const configDev = {
  username: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: 'books_database_development',
  host: process.env.MYSQL_HOST,
  dialect: 'mysql',
};

const configProd = {
  username: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: 'books_database_production',
  host: process.env.MYSQL_HOST,
  dialect: 'mysql',
};

const configTest = {
  username: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: 'books_database_test',
  host: process.env.MYSQL_HOST,
  dialect: 'mysql',
};

module.exports = {
  development: configDev,
  test: configTest,
  production: configProd,
};