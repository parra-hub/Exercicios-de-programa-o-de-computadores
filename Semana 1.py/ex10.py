def estatisca(lista):
    minimo=lista[0]
    maior=lista[0]
    cont=0
    media=0
    listanova=[]
    for i in range(len(lista)):
        if lista[i] <= minimo:
            minimo=lista[i]
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior=lista[i]
    for i in range(len(lista)):
        cont=cont+lista[i]
    media=cont/len(lista)
    return (media,minimo,maior)
lista=[]
for i in range(5):
    valor = int(input('informe os valores:'))
    lista.append(valor)

resultado=estatisca(lista)

media,min,max=resultado

print('maior numero:',max,'menor numero',min,'média:',media)
        