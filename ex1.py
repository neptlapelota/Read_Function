def leitura_do_arquivo():
    with open(r'E:\FIAP\PROGRAMAÇÃO\google clone\.py\Nova pasta\darkweb2017-top100.txt', 'r') as arquivo:
        senhas = arquivo.readlines()
        for i in range(10):
            print (senhas[i])

leitura_do_arquivo()