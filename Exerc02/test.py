from main import *

def test_lista_numeros_inteiros():
    entrada = [1, 2, 3, 4, 5]
    saida = lista_numeros_inteiros(entrada)

    assert saida == [2, 6, 6, 12, 10]