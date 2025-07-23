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
    def multa_localidade(velocidade: float) -> int:
    if velocidade <= 50:
        return 0
    elif velocidade <= 90:
        return 60
    elif velocidade < 120:
        return 120
    else:
        return 320
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
            if escolha == 1:
            multa = multa_localidade(velocidade)
            elif escolha == 2:
            multa = multa_fora_localidade(velocidade)
            if multa == 0:
                print("\nSem multa. Velocidade dentro do limite.")
            else:
                print(f"\nMulta aplicada: {multa}€")

            if multa == 0:
                print("\nSem multa. Velocidade dentro do limite.")
            else:
                print(f"\nMulta aplicada: {multa}€")

            # (vamos adicionar aqui a lógica de multas no próximo passo)
        else:
            print("Opção inválida!")
