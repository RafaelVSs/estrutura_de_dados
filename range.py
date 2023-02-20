# range(): função que gera uma faixa de números
# É muito usada em associação com listas

# range() com 1 parâmetro: gera uma faixa que vai 
# de 0 (zero) até o valor do parâmetro -1

for x in range(10):
    print(x)

print("*" * 80)

# range() com dois parametros: gera uma lista começando pelo
# primeiro parametro (inclusive) até o segundo argumento
# (exclusive, NÃO ENTRA)

for y in range(5, 12):
    print(y)
    
print("*" * 80)
    
# Range com 3 parametros:
# 1: limite inferior (inclusive)
# 2: limite superior (EXCLUSIVE)
# 3: passo (de quanto em quanto a lista vai saltar; PODE SER NEGATIVO)

for z in range(0, 22, 3): 
    print(z)
    
print("*" * 80)

# range() com passo negativo
for k in range(10, 0, -1):
    print(k)