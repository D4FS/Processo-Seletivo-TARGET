#QUESTAO 1

#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print (SOMA) #a SOMA no final será 91

#QUESTÃO 2

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


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

#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: • SP – R$67.836,43 • RJ – R$36.678,66 • MG – R$29.229,88 • ES – R$27.165,48 • Outros – R$19.849,53 Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

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

#5) Escreva um programa que inverta os caracteres de um string. IMPORTANTE: a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;


STRING  = input("Insira a string: ")

lista_de_caracteres = list(STRING)

lista_invertida = []
for char in lista_de_caracteres:
    lista_invertida.insert(0, char)


texto_invertido = ''.join(lista_invertida)

print("String invertida:", texto_invertido)




