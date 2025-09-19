chave={'a':2,'b':5,'c':5}
cont=0
for valor in chave.values():
    cont=valor+cont

print(f'A soma dos valores é:{cont}')