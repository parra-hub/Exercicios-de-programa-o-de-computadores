chave={}
notamaior=0
nome=0
while True:
    escolha=input('deseja cadastrar nota? responda Sim ou Não:')
    if escolha.lower() == 'não':
        break
    elif escolha.lower() == 'sim':
        aluno=input('informe o nome do aluno:')
        nota=float(input('informe a nota do aluno:'))
        chave.update({aluno:nota})
    else:
        print('responda apenas entre Sim ou Não')

for chave, valor in chave.items():
    if valor > notamaior:
        notamaior = valor
        nome=chave


print(f'maior nota é do(a) aluno(a):{nome} com {notamaior} pontos')
