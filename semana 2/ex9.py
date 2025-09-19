chave={'arroz': 5, 'feijão': 3, 'macarrão': 7}
print(f'escolha entre:{chave}')
escolha=input('informe o item que deseja:')

if escolha in chave:
    chave[escolha]-=1
    print('venda realizada')
    print('novo estoque:',chave)
else:
    print('item')