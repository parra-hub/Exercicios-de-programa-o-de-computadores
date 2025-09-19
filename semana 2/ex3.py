funcionario={}

nome1=input('digite o nome do funcionario ou digite sair para encerrar o cadastro:')
cargo1 = input('digite o cargo do funcionario;')
salario1=input('digite o salario:')
funcionario= {'nome':nome1,'cargo': cargo1,'salario': salario1}

print(funcionario)

escolha=input('deseja atualizar o salário cadastrado? Responda apenas com Sim ou Não:')

if escolha.upper() =='SIM':
    salarionovo=float(input('digite um novo salario:'))
    funcionario.update({'salario':salarionovo})
    print(funcionario)
else:
    print('fim')