def converter():
    abertura()
    escolher_opcao()


def abertura():
    print("**********************")
    print("* Conversor de Moeda *")
    print("**********************")


def escolher_opcao():
    print("\n*****************************************")
    print("* {1} Real -> Dólar x {2} Dólar -> Real *")
    print("*****************************************\n")
    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        print("\nConversão do Real (Brasil) para Dólar (Estados Unidos)\n")
        real = float(input("Digite o valor em Real que você deseja converter: "))
        conversao = float(input("Digite a cotação do Dólar no momento: "))
        convertido = real * conversao
        conversao_realizada_real_para_dolar(real, conversao, convertido)
    else:
        print("\nConversão do Dólar (Estados Unidos) para Real (Brasil)")
        dolar = float(input("Digite o valor em Dólar que você deseja converter: "))
        conversao = float(input("Digite a cotação do Real no momento: "))
        convertido = dolar * conversao
        conversao_realizada_dolar_para_real(dolar, conversao, convertido)


def conversao_realizada_real_para_dolar(real, conversao, convertido):
    print(f"\nOpção Escolhida: Conversão do Real (Brasil) para Dólar (Estados Unidos)")
    print(f"Valor definido para ser convertido: R${real}")
    print(f"Valor da Cotação do Dólar: ${conversao}")
    print(f"\nCom a cotação do Dólar atual, você pode adquirir ${round(convertido, 2)} com o valor de R${real}")


def conversao_realizada_dolar_para_real(dolar, conversao, convertido):
    print(f"\nOpção Escolhida: Conversão do Dólar (Estados Unidos) para Real (Brasil)")
    print(f"Valor definido para ser convertido: ${dolar}")
    print(f"Valor da Cotação do Real: R${conversao}")
    print(f"\nCom a cotação do Real atual, você pode adquirir R${round(convertido, 2)} com o valor de ${dolar}")
 

if __name__ == '__main__':
    converter()
