// VERSAO 1: DEFININDO SCHEMA
// ----------------------------------------------------------------

// import { Schema, model } from 'mongoose';

// const petSchema = new Schema({
//   name: { type: String, required: true },
//   species: { type: String, required: true },
//   age: { type: Number, required: false },
//   weight: { type: Number, required: true },
//   dailyMealsNumber: { type: Number, required: true, min: 2, max: 5 },
// });

// VERSAO 2: DEFININDO SCHEMA + MODEL
// ----------------------------------------------------------------

// import { Schema, model } from 'mongoose';

// const petSchema = new Schema({
//   name: { type: String, required: true },
//   species: { type: String, required: true },
//   age: { type: Number, required: false },
//   weight: { type: Number, required: true },
//   dailyMealsNumber: { type: Number, required: true, min: 2, max: 5 },
// });

// Como o próprio nome sugere, a função model(), usada no trecho de código anterior, cria uma Model para uma Collection. Essa função recebe como parâmetros, e nessa ordem, uma String contendo o nome da Collection e o Schema com o “molde” que definimos anteriormente.

// const Pet = model('Pet', petSchema);

// VERSAO 3: DEFININDO SCHEMA + MODEL + INTERFACES
// ----------------------------------------------------------------

import { Schema, model, connect } from 'mongoose';

// 1. Cria a interface que representa as informações de um Pet
interface IPet {
  name: string;
  species: string;
  age?: number; //Campo opcional definido por: (?)
  weight: number;
  dailyMealsNumber: number;
}

// 2. Cria o Schema de acordo com Interface por meio do Generic: <IPet>
const petSchema = new Schema<IPet>({
  name: { type: String, required: true },
  species: { type: String, required: true },
  age: { type: Number, required: false },
  weight: { type: Number, required: true },
  dailyMealsNumber: { type: Number, required: true, min: 2, max: 5 },
});

// 3. Cria a Model de acordo com a Interface e o Schema
const Pet = model<IPet>('Pet', petSchema); // Aceita somente schemas do tipo IPet
