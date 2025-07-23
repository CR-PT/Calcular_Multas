def menu():
    print("\nOnde circulava o veículo?")
    print("Escolha uma opção:")
    print("1 - Localidade")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")
    print("0 - Sair")
    try:
        return int(input("Introduza o local: "))
    except ValueError:
        return -1

def obter_velocidade():
    try:
        return float(input("Introduza a velocidade do veículo (km/h): "))
    except ValueError:
        print("Valor inválido! Tente novamente.")
        return obter_velocidade()

# Chamada inicial
if __name__ == "__main__":
    while True:
        escolha = menu()
        if escolha == 0:
            print("Programa encerrado.")
            break
        elif escolha in (1, 2, 3):
            velocidade = obter_velocidade()
            # (vamos adicionar aqui a lógica de multas no próximo passo)
        else:
            print("Opção inválida!")
