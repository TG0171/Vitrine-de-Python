# PROGRAMA DE CADASTRO DE ALUNOS - TESTE

# IMPORTANDO A DATA ATUAL
from datetime import datetime, timezone

# Obtenção da data atual e formatação
data_e_hora_atuais = datetime.now() 
data_formatada = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")

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

curso_escolhido = ""
unidade_escolhida = ""

def cadastrar_curso():
    global curso_escolhido
    print("******** CURSOS DISPONÍVEIS ********")
    cursos_disponiveis = {
        "01": "Programação em Python",
        "02": "Programação Front-End",
        "03": "Pacote Office",
        "04": "Canva Profissional"
    }
    for codigo, curso in cursos_disponiveis.items():
        print(f"{curso} [{codigo}]")
    while True:
        codigo_curso = input("Digite o código do curso desejado: ")
        if codigo_curso in cursos_disponiveis:
            curso_escolhido = cursos_disponiveis[codigo_curso]
            break
        else:
            print("Escolha uma opção válida!")

def cadastrar_unidade():
    global unidade_escolhida
    print("******** UNIDADES FUNDAÇÃO RUBEN BERTA ********")
    unidades_disponiveis = {
        "01": "Centro",
        "02": "Jacarecanga",
        "03": "Parangaba"
    }
    for codigo, unidade in unidades_disponiveis.items():
        print(f"{unidade} [{codigo}]")
    while True:
        codigo_unidade = input("Digite o código da unidade escolhida: ")
        if codigo_unidade in unidades_disponiveis:
            unidade_escolhida = unidades_disponiveis[codigo_unidade]
            break
        else:
            print("Escolha uma opção válida!")

def cadastrar_aluno():
    global curso_escolhido, unidade_escolhida
    nome = input("Insira o nome do aluno: ")
    cpf = input("Insira o CPF do aluno: ")
    endereco = input("Insira o endereço do aluno: ")
    email = input("Insira o e-mail do aluno: ")
    telefone = input("Insira o número de telefone do aluno: ")
    while True:
        try:
            idade = int(input("Insira a idade do aluno: "))
            if 15 <= idade <= 29:
                print(f"Aluno {nome} matriculado com sucesso!")
                print(f"O aluno {nome} foi matriculado com sucesso em {data_formatada} pelo funcionário {login} no curso de {curso_escolhido} na unidade {unidade_escolhida}.")
                break
            else:
                print(f"Aluno {nome} não pôde ser matriculado devido à idade não permitida.")
        except ValueError:
            print("Por favor, insira uma idade válida.")

# FUNÇÃO PRINCIPAL
def main():
    global curso_escolhido, unidade_escolhida
    while True:
        cadastrar_curso()
        cadastrar_unidade()
        cadastrar_aluno()
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

# Chamada da função principal
if __name__ == "__main__":
    main()
