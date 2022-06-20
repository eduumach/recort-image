import os

from PIL import Image
from numpy import asarray
import numpy as np


def delete(pasta):
    # pasta = '/home/dudu/Projetos/Github/bataset/deteccao_de_graos/data/obj_train_data/'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if ".txt" in arquivo:
                with open(pasta + arquivo, 'r') as writer:
                    if len(writer.read()) < 3:
                        os.remove(pasta + arquivo)
                        os.remove(pasta + arquivo.replace(".txt", ".PNG"))

                # print(os.path.join(diretorio, arquivo))


def divide(pasta, image_name, local):
    image = Image.open(local)
    array = asarray(image)

    matriz = np.array_split(array, 2)

    Image.fromarray(matriz[0]).save(pasta + "0" + image_name)
    Image.fromarray(matriz[1]).save(pasta + "1" + image_name)


def anotacao(pasta, file, anotacao_file):
    arquivo1 = open(pasta + '0' + file, 'w')
    arquivo2 = open(pasta + '1' + file, 'w')

    with open(anotacao_file, 'r') as writer:
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


pasta = '/home/dudu/Projetos/Github/bataset/data/'
teste = '/home/dudu/Projetos/Github/bataset/teste/'
train = open("./train.txt", 'w')
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if ".txt" in arquivo:
            with open(pasta + arquivo, 'r') as writer:
                divide(teste, arquivo.replace(".txt", ".PNG"), pasta + arquivo.replace(".txt", ".PNG"))
                anotacao(teste, arquivo, pasta + arquivo)
                train.write("data/obj_train_data/" + "0" + arquivo.replace(".txt", ".PNG") + "\n"
                            + "data/obj_train_data/" + "1" + arquivo.replace(".txt", ".PNG") + "\n")
