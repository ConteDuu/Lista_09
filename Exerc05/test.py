from funcoes import *

def test_produtos_comprados():
    produtos = [
        {"nome": "carne", "valor": 35, "qtde": 3},
        {"nome": "arroz", "valor": 40, "qtde": 1},
        {"nome": "feijão", "valor": 12, "qtde": 2},
    ]

    saida = lista_produtos_comprados(produtos)

    assert saida == {
        "produtos": [
            {"nome": "carne", "valor": 35, "qtde": 3, "total": 105},
            {"nome": "arroz", "valor": 40, "qtde": 1, "total": 40},
            {"nome": "feijão", "valor": 12, "qtde": 2, "total": 24},
        ],
        "total": 169
    }