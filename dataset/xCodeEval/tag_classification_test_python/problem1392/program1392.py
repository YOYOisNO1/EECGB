def program1392():
    gnomos = int(input())
    resposta = (3 ** (3 * gnomos) - 7 ** gnomos) % ((10 ** 9) + 7)
    print(resposta)