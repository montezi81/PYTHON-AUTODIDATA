# Set
numeros = [2,2,5,8]
frutas = {'maça', 'uva', 'banana', 'morango', 'maça'}

set_numeros = set (numeros)
set_frutas = set (frutas)
# O Set remove os valores repetidos dentro da lista
print(set_numeros)
print(set_frutas)

# Adicionar valores
set_numeros.add(10)
set_frutas.add('Pera')
print(set_numeros)
print(set_frutas)

# Conjuntos
numeros1 = [2,2,5,8]
numeros2 = [2,2,3,9]
a = set(numeros1)
b = set(numeros2)
# União das duas listas eliminando os repetidos
# quero somente os valores que estão contidos em um e não no outro
print(a.symmetric_difference(b))
# Intercessão são os valores comuns entres os sets de a e b
print(a.intersection(b))
# removemos os duplicados e temos somente os valores unicos
print(a.union(b))

