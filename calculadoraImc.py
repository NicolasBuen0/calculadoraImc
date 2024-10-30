def calcular_imc(peso, altura):
    """Função para calcular o IMC."""
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return "Altura não pode ser zero."

def classificar_imc(imc):
    """Função para classificar o IMC de acordo com o valor."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    print("Calculadora de IMC")
    try:
        peso = input("Digite o seu peso em kg: ")
        altura = input("Digite a sua altura em metros (ou cm): ")

        # Substituir vírgula por ponto e converter para float
        peso = float(peso.replace(",", "."))
        altura = float(altura.replace(",", "."))
        
        # Convertendo altura para metros se o valor for dado em centímetros
        if altura > 3:  # Assumimos que valores acima de 3 são em centímetros
            altura /= 100
        
        imc = calcular_imc(peso, altura)
        if isinstance(imc, float):
            print(f"Seu IMC é: {imc:.2f}")
            print("Classificação:", classificar_imc(imc))
        else:
            print(imc)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
