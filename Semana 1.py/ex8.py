vogais = ('a', 'e', 'i', 'o', 'u')
cont=0
valor=input('digite uma vogal:')
for i,numero in enumerate(vogais):
    if valor == numero:
        cont=i

print('A vogal',valor,'esta na posição',cont)