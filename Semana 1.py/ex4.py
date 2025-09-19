animais=('porco','vaca','galinha','peixe')
cont=0
cont2=0
animal=input('escolha um animal entre, porco, vaca, galinha, peixa: ')

for i in range(len(animais)):
    if animal == animais[i]:
        cont=animal
        cont2=i

print('animal:',cont,'/indice:',cont2)