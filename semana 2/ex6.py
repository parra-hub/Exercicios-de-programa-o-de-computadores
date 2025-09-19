roupas={'camisa':89,'calça':102,'oculos':100}
print('produtos disponiveis: camisa, calça, oculos')

escolha=input('escolha qual deseja remover:')
if escolha.lower() == 'camisa' or escolha == 'calça' or escolha == 'oculos':
    valor=roupas.pop(escolha)
    print('produto removido:',valor)
    print(roupas)
else:
    print('produto não encontrado')
    print(roupas)