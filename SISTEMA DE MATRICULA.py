# PROGRAMA DE CADASTRO DE ALUNOS - TESTE

# LOGIN DE FUNCIONÁRIO
print("******** FUNDAÇÃO RUBEN BERTA ********")
login = input("Insira a sua credencial de acesso: ")
senha = input("Insira sua senha de acesso: ")

# Verificando credenciais
if senha == "26007" and login == "FUNC01":
    print(f"ACESSO AUTORIZADO, PROSSIGA, {login}.")
else:
    print("ACESSO NEGADO!")
    exit()

curso = ""  # Variável global para armazenar o curso escolhido
unidade = ""  # Variável global para armazenar a unidade escolhida

def cadastro_curso():
    global curso
    print("******** CURSOS DISPONÍVEIS ********")
    print("Programação em Python [01]")
    print("Programação Front-End [02]")
    print("Pacote Office [03]")
    print("Canva Profissional [04]")
    cadastro_curso = input("Digite o curso desejado: ")
    if cadastro_curso == "01":
        curso = "Programação em Python"
    elif cadastro_curso == "02":
        curso = "Programação Front-End"
    elif cadastro_curso == "03":
        curso = "Pacote Office"
    elif cadastro_curso == "04":
        curso = "Canva Profissional"
    else:
        print("Escolha uma opção válida!")

def cadastro_unidade():
    global unidade
    print("******** UNIDADES FUNDAÇÃO RUBEN BERTA ********")
    print("Unidade Centro [01]")
    print("Unidade Jacarecanga [02]")
    print("Unidade Parangaba [03]")
    cadastro_unidade = input("Digite a unidade escolhida: ")
    if cadastro_unidade == "01":
        unidade = "Centro"
    elif cadastro_unidade == "02":
        unidade = "Jacarecanga"
    elif cadastro_unidade == "03":
        unidade = "Parangaba"
    else:
        print("Escolha uma opção válida!")

def cadastrar_aluno():
    global curso, unidade
    nome = input("Insira o nome do aluno: ")
    cpf = input("Insira o CPF do aluno: ")
    data = input("Digite a data de hoje: ")
    endereco = input("Insira o endereço do aluno: ")
    email = input("Insira o e-mail do aluno: ")
    telefone = input("Insira o número de telefone do aluno: ")
    idade = int(input("Insira a idade do aluno: "))
    if 15 <= idade <= 29:
        print(f"Aluno {nome} matriculado com sucesso!")
        print(f"O aluno {nome} foi matriculado com sucesso no dia {data} pelo (a) funcionário (a) {login} no curso de {curso} na unidade {unidade}.")
    else:
        print(f"Aluno {nome} não pôde ser matriculado devido à idade não permitida.")

# FUNÇÃO PRINCIPAL
def main():
    global curso, unidade
    while True:
        cadastro_curso()
        cadastro_unidade()
        cadastrar_aluno()
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

# Chamada da função principal
if __name__ == "__main__":
    main()
