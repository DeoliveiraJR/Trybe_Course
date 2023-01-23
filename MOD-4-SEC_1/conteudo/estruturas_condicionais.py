# Menor que R$2.000,00, pessoa desenvolvedora estagiária;

# Entre R$2.000,00 e R$5.800,00, pessoa desenvolvedora júnior;

# Entre R$5.800,00 e R$7.500,00, pessoa desenvolvedora pleno;

# Entre R$7.500,00 e R$10.500,00, pessoa desenvolvedora sênior;

# Qualquer valor acima do que já foi mencionado a pessoa desenvolvedora é considerada liderança.

position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# Em alguns casos, em que não seja prejudicada a legibilidade, podemos criar estruturas de mapeamento (dicts) para simplificar o aninhamento de condicionais. Como o exemplo a seguir:

key = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
print(from_to[key])
