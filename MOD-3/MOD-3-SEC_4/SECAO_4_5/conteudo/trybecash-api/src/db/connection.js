// src/db/connection.js

// ⚠️ Atenção: toda vez que uma variável de ambiente é alterada, é necessário parar e reiniciar a aplicação, mesmo quando se utiliza o nodemon, pois estas variáveis de ambiente, por serem temporárias, são “carregadas” uma única vez no momento em que a aplicação é executada.

const mysql = require('mysql2/promise');

const connection = mysql.createPool({
  host: process.env.MYSQL_HOST,
  port: process.env.MYSQL_PORT,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DATABASE_NAME,
  waitForConnections: process.env.MYSQL_WAIT_FOR_CONNECTIONS,
  connectionLimit: process.env.MYSQL_CONNECTION_LIMIT,
  queueLimit: process.env.MYSQL_QUEUE_LIMIT,
});

module.exports = connection;
