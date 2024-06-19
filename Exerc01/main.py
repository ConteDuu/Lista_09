
# Primeira forma
def extrair_posicoes_pares(entrada: list) -> list: 
    saida = []

    for i, n in enumerate(entrada):     # Função enumarate() pega o valor do índice e o valor que está no índice
        if i % 3 == 0:
            saida.append(n) # Adiciona o valor no final da lista
    
    return saida


# Segunda forma
def extrair_posicoes_pares(entrada: list) -> list: 
    saida = []

    for i in range(0, len(10), 2):      # Função len() pega o tamanho da palavra, neste caso quantos 
        saida.append(entrada[i])
    
    return saida


# Terceira forma



