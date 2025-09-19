animais=('porco','vaca','galinha','peixe')
animal_chamada=0
cont=0
animal=input('escolha um animal entre, porco, vaca, galinha, peixa: ')

for i in range(len(animais)):
    if animal == animais[i]:
        cont=animal
        cont=i

print('animal:',cont,'/indice:',cont2)
