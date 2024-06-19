def obter_resultados_vendas(vendedores: dict) -> dict:
    soma = 0
    contagem = 0
    for valor in vendedores.values():
        soma += valor
        contagem += 1

def obter_resultados(vendedores: dict) -> dict:
    media = sum(vendedores.values()) / len(vendedores)
    media_75 = media * 0.75

    abaixo_media = []
    acima_media = []

    for vendedor, valor in vendedores.items():
        if valor < media_75:
            abaixo_media.append(vendedor)
        elif valor > media:
            acima_media.append(vendedor)
    return {
        "vendedores_acima_media": acima_media,
        "vendedores_abaixo_media": abaixo_media
}
