def analisar_humidor(leituras):
    alerta = 0
    soma = 0
    contagem = 0
    for l in leituras:
        if l < 65 or l > 70:
            alerta += 1
        else:
            soma += l
            contagem += 1
    media = soma / contagem if contagem > 0 else 0
    print(f"Alerta: {alerta} leituras fora da faixa. Média válida: {media:.2f}%")

if __name__ == "__main__":
    dados = [68, 69, 72, 66, 64, 70, 65]
    analisar_humidor(dados)