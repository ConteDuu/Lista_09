from main import *

def test_transformar_lista():
    saida = test_transformar_lista([15, 8, 12, 9, 20])
    assert saida == [14, 22, 34, -25, -5]