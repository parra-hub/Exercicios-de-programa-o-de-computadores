tupla=(1,1,2,3,1,2,3,4,1,2,3)
usuario=int(input('informe um valor'))
cont=0
for i in range(len(tupla)):
    if usuario == tupla[i]:
        cont=cont+1

print('O numero:',usuario,'aparece:',cont,'vezes na lista')