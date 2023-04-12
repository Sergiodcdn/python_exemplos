class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.bonus = 0
    
    def __str__(self):
        return f"{self.nome}, salário: {self.salario}, bônus: {self.bonus}"
    
    def __eq__(self, outro):
        return self.nome == outro.nome and self.salario == outro.salario
    
    def __lt__(self, outro):
        return self.salario < outro.salario
    
    def __add__(self, valor):
        self.bonus += valor
    
    def __sub__(self, valor):
        self.bonus -= valor
    
    def __call__(self):
        return self.salario + self.bonus
    
    def __repr__(self):
        return f"Funcionario('{self.nome}', {self.salario})"
    

def cadastrar_funcionarios():
    lista_funcionarios = []
    while True:
        nome = input("Digite o nome do funcionário (ou 'fim' para sair): ")
        if nome == "fim":
            break
        salario = float(input("Digite o salário do funcionário: "))
        funcionario = Funcionario(nome, salario)
        lista_funcionarios.append(funcionario)
    return lista_funcionarios
    

def mostrar_funcionarios(lista_funcionarios):
    print("Funcionários cadastrados:")
    for funcionario in lista_funcionarios:
        print(funcionario)
    

def atualizar_bonus(lista_funcionarios):
    while True:
        nome = input("Digite o nome do funcionário para atualizar o bônus (ou 'fim' para sair): ")
        if nome == "fim":
            break
        for funcionario in lista_funcionarios:
            if funcionario.nome == nome:
                valor = float(input("Digite o valor do bônus: "))
                funcionario.bonus += valor
                print(f"Bônus atualizado para {funcionario.bonus} para {funcionario.nome}")
                break
        else:
            print(f"Funcionário {nome} não encontrado")
    

def ordenar_funcionarios(lista_funcionarios):
    print("Ordenando por salário:")
    for funcionario in sorted(lista_funcionarios):
        print(funcionario)
    

lista_funcionarios = cadastrar_funcionarios()

while True:
    opcao = input("Digite a opção desejada (1 - mostrar funcionários, 2 - atualizar bônus, 3 - ordenar por salário, 4 - sair): ")
    if opcao == "1":
        mostrar_funcionarios(lista_funcionarios)
    elif opcao == "2":
        atualizar_bonus(lista_funcionarios)
    elif opcao == "3":
        ordenar_funcionarios(lista_funcionarios)
    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente")
