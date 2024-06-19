
def obeter_valor(atual: int, anterior:int) -> int :
    if atual % 2 == 0:
        return atual + anterior
    return atual - anterior

def gerar_lista_(entrada:list) -> list:
    saida = []
    for posicao, valor_na_posicao in enumerate(entrada):
        if valor_na_posicao == 0:
            if valor_na_posicao % 2 == 0:
                saida.append(valor_na_posicao + 2)
            else:
                saida.append(valor_na_posicao - 1)
        elif valor_na_posicao % 2 == 0:
            saida.append(valor_na_posicao + saida[posicao - 1])
        else:
            saida.append(valor_na_posicao - saida[posicao - 1])
    return saida
