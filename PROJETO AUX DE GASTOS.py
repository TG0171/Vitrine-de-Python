#FUNÇÃO DE CALC. DE GASTOS TOTAIS 
def calcular_gastos_totais(gastos):
    total = 0
    for gasto in gastos.values():
        total += gasto
    return total

#FUNÇÃO PRINCIPAL
def main():
    # Pedindo ao usuário para inserir os gastos
    gastos = {}

    gastos["água"] = float(input("Insira o gasto com água e saneamento: "))
    gastos["eletricidade"] = float(input("Insira o gasto com eletricidade: "))
    gastos["telefonia"] = float(input("Insira o gasto com telefonia: "))
    gastos["internet"] = float(input("Insira o gasto com internet: "))
    gastos["alimentação"] = float(input("Insira o gasto com alimentação: "))
    gastos["lazer"] = float(input("Insira o gasto com lazer: "))
    gastos["combustíveis"] = float(input("Insira o gasto com combustível: "))
    gastos["outros"] = float(input("Insira outros gastos: "))

    #CALCULANDO OS GASTOS TOTAIS
    total_gastos = calcular_gastos_totais(gastos)

    #EXIBINDO OS GASTOS
    print("\n=== Informações de gastos ===")
    for categoria, valor in gastos.items():
        print(f"{categoria.capitalize()}: R$ {valor:.2f}")
    print(f"\nTotal de gastos mensais: R$ {total_gastos:.2f}")

#FUNÇÃO PRINCIPAL
if __name__ == "__main__":
    main()
