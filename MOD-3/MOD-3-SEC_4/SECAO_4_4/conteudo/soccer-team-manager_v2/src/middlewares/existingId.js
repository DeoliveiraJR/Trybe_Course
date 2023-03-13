// src/middlewares/existingId.js

// const existingId = (req, res, next) => {
//   const id = Number(req.params.id);
//   if (teams.some((t) => t.id === id)) {
//     // se existe, a requisição segue para o próximo middleware
//     next();
//   } else {
//     // se não existe, então vamos retornar o status HTTP 404
//     res.sendStatus(404);
//   }
// };

// Para fixar
// Agora é sua vez. Modifique o código do middleware existingId para retornar o http status 404 e um objeto no formato { message: 'Time não encontrado' } quando não encontrar o time com o id recebido.
const existingId = (req, res, next) => {
  const id = Number(req.params.id);
  if (!teams.some((t) => t.id === id)) {
    return res.sendStatus(404).json({ message: 'Time não encontrado' });
  }
  next();
};


module.exports = existingId;