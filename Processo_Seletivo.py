#QUESTAO 1

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print (SOMA) #a SOMA no final será 91

#QUESTÃO 2

def pertence_fibonacci(x):
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

n = int(input('INSIRA UM NUMERO: '))
if pertence_fibonacci(n):
    print(f"{n} pertence a sequencia")
else:
    print(f"{n} não pertence a sequencia")


#QUESTAO 4

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

import math

TOTAL = sum(faturamento.values())

PORCETAGEM = {estado: (valor/TOTAL) * 100 for estado, valor in faturamento.items()}
print(f"Valor total mensal: R${TOTAL:.2f}")
for estado, percentual in PORCETAGEM.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")


#QUESTAO 5


STRING  = input("Insira a string: ")

lista_de_caracteres = list(STRING)

lista_invertida = []
for char in lista_de_caracteres:
    lista_invertida.insert(0, char)


texto_invertido = ''.join(lista_invertida)

print("String invertida:", texto_invertido)




