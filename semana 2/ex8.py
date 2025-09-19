palavra=input('digite uma palavra:')
chave={}
for letras in palavra:
    if letras in chave:
        chave[letras]+=1
    else:
        chave[letras] = 1
print(chave)