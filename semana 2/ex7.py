chave1={}
chave2={}
chaves={}
for i in range(4):
    chave=input('adicione o nome da chave:')
    valor=input('digite o valor do input')
    if i < 2:
        chave1.update({chave:valor})
    else:
        chave2.update({chave:valor})

print(f'chave1 = {chave1}')
print(f'chave2 = {chave2}')


for chave, valor in chave1.items():
    chaves.update({chave:valor})
for chave, valor in chave2.items():
    chaves.update({chave:valor})

print(f'chaves juntas:{chaves}')