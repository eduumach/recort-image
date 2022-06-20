def anotacao(anotacao):
    arquivo1 = open('0'+anotacao, 'w')
    arquivo2 = open('1'+anotacao, 'w')

    with open('frame_000000.txt', 'r') as writer:
        anotacoes = writer.readlines()

        for anotacao in anotacoes:
            anotacao = anotacao.strip().split(' ')

            if float(anotacao[2]) <= 0.5:
                x = (int(float(anotacao[1]) * 1080)) / 1080
                y = (int(float(anotacao[2]) * 1920)) / 960
                w = (int(float(anotacao[3]) * 1080)) / 1080
                h = (int(float(anotacao[4]) * 1920)) / 960
                arquivo = arquivo1
            else:
                x = (int(float(anotacao[1]) * 1080)) / 1080
                y = (int(float(anotacao[2]) * 1920) - 960) / 960
                w = (int(float(anotacao[3]) * 1080)) / 1080
                h = (int(float(anotacao[4]) * 1920)) / 960
                arquivo = arquivo2

            lista = [anotacao[0], str(x), str(y), str(w), str(h)]

            arquivo.write(" ".join(lista) + "\n")


    arquivo1.close()
    arquivo2.close()
