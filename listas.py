import math
# LISTAS EM PYTHON
# Listas são uma forma de armazenar mis de um valor em uma
# unica variável. Os valores podem ser de tipos diferentes.

# Uma lista de números
valores = [2, 3, 5, 7, 9, 11, "batata", "tomate", True]

#OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro até
#    o último elemento, fazendo algo com cada um deles.
#    No caso a seguir, vamos exibir cada um dos elementos
#    separadamente usando print().
for val in valores:
    print(val)

print("*" * 80)

# 2) INSERÇÃO DE UM ELEMENTO NO *FIM* DA LISTA: append()
valores.append("cebola")
print(valores)

valores.append(29)
print(valores)

print("*" * 80)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICA: insert()
#    Parâmetros:
#    1°) posição para inserir (contagem inicia em 0)
#    2°) valor a ser inserido
valores.insert(4, "chuchu")    #Insere "chuchu" na 5ª posição
print(valores)

valores.insert(0, "abobrinha")    #Insere "abobrinha" na 1ª posição
print(valores)

print("*" * 80)

# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print("Elemento da SÉTIMA posição: ", valores[6])
print("Elemento da TERCEIRA posição: ", valores[2])
print("Elemento da PRIMEIRA posição: ", valores[0])
print("Elemento da ÚLTIMA posição: ", valores[-1])
print("Elemento da PENULTIMA posição: ", valores[-2])

print("*" * 80)

# 5) SUBSTITUINDO VALORES EXISTENTES
print("ANTES: ", valores)

#    Substituindo o valor da posição 10
valores[10] = "cenoura"

#    Substituindo o valor da posição 0
valores[0] = "beterraba"

#    Substituindo o valor da última posição
valores[-1] = "alho"
print("DEPOIS: ", valores)

print("*" * 80)

# 6) DETERMINANDO QUANTOS ELEMENTOS HÁ NA LISTA: len()
print("Ultimo valor da lista: ", valores[len(valores) - 1])
print(valores)

print("*" * 80)

# 7) REMOVENDO O ÚLTIMO ELEMENTO DA LISTA: pop()
print("Antes: ", valores)
ultimo = valores.pop()
print("Valor removida da lista: ", ultimo)
print("Depois: ", valores)

print("*" * 80)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
print("Antes: ", valores)
pos9 = valores.pop(9)    #  REMOVE O ELEMENTO DA POSIÇÃO 9
print("Valore removida da posição 9: ", pos9)
pos0 = valores.pop(0)    #  REMOVE O PRIMEIRO ELEMENTO (posição 0)
print("Valore removida da primeira posição: ", pos0)
print("Depois: ", valores)

print("*" * 80)

# 9) REMOVENDO UM ELEMENTO PELO SEU VALOR: REMOVE()
print("Antes: ", valores)
valores.remove("batata")    #  REMOVE O VALOR "batata"
valores.remove(5)           #  REMOVE O VALOR 5
print("Depois: ", valores)

print("*" * 80)

# Acrescentando mais alguns elementos na lista
valores.append(13)
valores.append(15)
valores.append("milho")
valores.append(17)
valores.append(19)

print("*" * 80)

# 10) FATIANDO UMA LISTA
print(valores)

# Cria uma sublista que contém os elementos de 0 até
# a posição 7 (posição 2 e 8 NÃO ENTRA)
sublista0_7 = valores[0:7]
print("Sublista da primeira posição até a sétima: ", sublista0_7)

# Cria uma sublista que contém os elementos do início
# até a posição 5 (posição 6 NÃO ENTRA)
sublista0_5 = valores[:6]
print("Sublista de 0 a 5: ", sublista0_5)

# Cria uma sublista que contém os elementos da posição 10
# até o fim da lista
sublista10_fim = valores[10:]
print("Sublista de 10 até o final: ", sublista10_fim)
