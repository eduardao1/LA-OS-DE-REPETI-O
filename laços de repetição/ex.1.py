positivo=0 
negativo=0
for i in range(20):
    n = int(input("Digite os numeros:"))
    if n>=0: positivo+=n
    else: negativo+=1 
print("valor positivo:", positivo)
print("valor dos negativos:",negativo)
