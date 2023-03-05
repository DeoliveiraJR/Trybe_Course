// `Interface`: Enrollable
// `Attributes`:
//     - enrollment: identificador único da matrícula
// `Methods`:
//     - generateEnrollment: retorna uma string única gerada como matrícula

// Enrollable.ts

export default interface Enrollable {
    enrollment: string;
    generateEnrollment(): string;
  }