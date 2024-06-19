
def lista_numeros_inteiros(entrada: list) -> list:
    saida = []
    for posicao, valor_no_indice in enumerate(entrada):
        if posicao % 2 == 0:
           saida.append(valor_no_indice * 2)
        else: 
            saida.append(valor_no_indice * 3)
    return saida