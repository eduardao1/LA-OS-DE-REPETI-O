#EduardoGomes,HeitorPernet,MatheusJóse PROVA 2 - Questão 4
num = int(input("Digite um número: "))
invertido = 0
real = num

while real > 0 :
    digito = real % 10
    invertido = invertido * 10 + digito
    real = real // 10
print("Número invertido:", invertido)
if num == invertido:
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")