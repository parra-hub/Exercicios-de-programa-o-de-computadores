qprint('escolha 1 para tabuada automatica com for:')
print('escolha 2 para tabuada manual com while:')
escolha=int(input('escolha:'))

if escolha == 1:
    escolha=int(input('escolha um valor para tabuada:'))
    for i in range(1,11):
        print(f'{escolha} x {i} = {escolha*i}')
elif escolha == 2:
    escolha=int(input('escolha um valor para tabuada:'))
    i = 1
    while i < 11:
        print(f'{escolha} x {i} = {escolha*i}')
        i += 1
else:
    print('erro')
