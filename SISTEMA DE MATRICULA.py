#PROGRAMA DE CADASTRO DE ALUNOS - TESTE

#LOGIN DE FUNCIONÁRIO
print("******** FUNDAÇÃO RUBEN BERTA ********")
login = input("Insira a sua credencial de acesso: ")
senha = int(input("Insira sua senha de acesso: "))

if senha == 26007 and login == "FUNC01":
    print(f"ACESSO AUTRIZADO, PROSSIGA, {login}.")
else: 
    print("ACESSO NEGADO!")
    exit()
    
def cadastrar_aluno():
    #INSERINDO DADOS
    nome = input("Insira o nome do aluno: ")
    cpf = input("Insira o CPF do aluno: ")
    data = input("Digite a data de hoje: ")
    curso = input("Digite o curso ao qual o aluno será matriculado: ")
    unidade = input("Qual será a unidade de ensino do aluno?: ")
    endereco = input("Insira o endereço do aluno: ")
    email = input("Insira o e-mail do aluno: ")
    telefone = input("Insira o número de telefone do aluno: ")
    idade = int(input("Insira a idade do aluno: "))

    #VERIFICAÇÃO DE IDADE
    if 15 <= idade <= 29:
        print(f"Aluno {nome} matriculado com sucesso!")
    else:
        print(f"Aluno {nome} não pôde ser matriculado devido à idade não permitida.")
        
    if 15 <= idade <= 29:
        print(f"O aluno {nome} foi matrículado com sucesso no dia {data} pelo (a) funcionário (a) {login} no curso de {curso} na unidade {unidade}.")

#FUNÇÃO PRINCIPAL
def main():
    while True:
        cadastrar_aluno()
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

#FUNÇÃO PRINCIPAL
if __name__ == "__main__":
    main()
