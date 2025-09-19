contatos={}

while True:
    nome=input('informe um nome ou sair para encerrar o cadastro:')
    if nome.upper() == 'SAIR':
        break
    telefone=input('Informe o telefone que deseja cadastrar')
    contatos[nome] = telefone

escolha=input('escolha qual nome quer consultar:')

print(escolha,'=',contatos.get(escolha,'nome não cadastrado'))