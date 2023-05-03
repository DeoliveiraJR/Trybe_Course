# A leitura do conteúdo de um arquivo pode ser feita utilizando a função read.
# Para experimentar, vamos escrever em um arquivo e lê-lo logo em seguida!

# escrita
file = open("arquivo.txt", mode="w")
file.write("Trybe S2")
file.close()

# leitura
file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()  # não podemos esquecer de fechar o arquivo

# Um arquivo é também um iterável, ou seja, pode ser percorrido em um laço de
# repetição. A cada iteração, uma nova linha é retornada. Vamos fazer igual ao
# exemplo anterior, porém dessa vez vamos escrever mais de uma linha!
# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    print(
        line
    )  # não esqueça que a quebra de linhatambém é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo

# Além de arquivos textuais (como os que manipulamos até agora), também
# existem arquivos binários. Eles são arquivos que contêm uma série de bytes e
# a sua leitura pode variar de acordo com o arquivo. Nesse caso, devemos
# acrescentar um b ao parâmetro mode,
# indicando que será utilizado o modo binário.

# As operações são similares a de um arquivo textual. Porém tanto a escrita
# quanto a leitura devem ser feitas utilizando bytes.
# escrita
file = open("arquivo.dat", mode="wb")
# o prefixo b em uma string indica que seu valor está codificado em bytes
file.write(b"C\xc3\xa1ssio 30")
file.close()

# leitura
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # saída: b'C\xc3\xa1ssio 30'
file.close()  # não podemos esquecer de fechar o arquivo

# Exercício 3:
# Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que:

# lê todas essas informações;
# aplique um filtro, mantendo somente as pessoas que estão reprovadas;
# escreva seus nomes em outro arquivo.
# Considere que a nota miníma para aprovação é 6.
recovery_students = []
with open("file.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recovery_students.append(student_grade[0] + "\n")


with open("recuStudents.txt", mode="w") as recu_students_file:
    print(recovery_students)
    recu_students_file.writelines(recovery_students)
