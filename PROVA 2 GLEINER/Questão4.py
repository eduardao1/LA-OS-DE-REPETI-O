#EduardoGomes,HeitorPernet,MatheusJóse PROVA 2 - Questão 4

num = int(input("digite um número inteiro: "))
soma = 0
real = num
cont = 0

#variavel soma foi usada para armazenar a soma dos dígitos
#num pro usuario digitar um numero inteiro
#usei o real para fazer uma copia do numero digitado e manter o original
#cont para contar a quantidade de digitos

while real > 0 :
    digito = real % 10
    soma = soma + digito
    real = real // 10

#aqui o while vai rodar enquanto o numero real for maior que 0
#o digito recebe o resto da divisao do numero real por 10
#soma recebe ela mesma mais o digito
#real recebe o resultado da divisao inteira de real por 10

cont == cont + 1 #conta a quantidade de digitos
resto = soma // cont #calcula o resto da divisao da soma pela quantidade de digitos
print("Resto da divisão de", soma, "por", cont, "é:", resto)

