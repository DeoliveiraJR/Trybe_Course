# Menor que R$2.000,00, pessoa desenvolvedora estagiária;

# Entre R$2.000,00 e R$5.800,00, pessoa desenvolvedora júnior;

# Entre R$5.800,00 e R$7.500,00, pessoa desenvolvedora pleno;

# Entre R$7.500,00 e R$10.500,00, pessoa desenvolvedora sênior;

# Qualquer valor acima do que já foi mencionado a pessoa desenvolvedora é considerada liderança.

SALARY = 100

POSITION = ""
if SALARY <= 2000:
    POSITION = "estagiário"
elif 2000 < SALARY <= 5800:
    POSITION = "júnior"
elif 5800 < SALARY <= 7500:
    POSITION = "pleno"
elif 7500 < SALARY <= 10500:
    POSITION = "senior"
else:
    POSITION = "líder"

# Em alguns casos, em que não seja prejudicada a legibilidade, podemos criar estruturas
# de mapeamento (dicts) para simplificar o aninhamento de condicionais. Como o exemplo a seguir:

KEY = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
print(from_to[KEY])
