import os
pasta = '/home/dudu/Projetos/Github/bataset/deteccao_de_graos/data/obj_train_data/'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if ".txt" in arquivo:
            with open(pasta + arquivo, 'r') as writer:
                if len(writer.read()) < 3:
                    os.remove(pasta + arquivo)
                    os.remove(pasta + arquivo.replace(".txt", ".PNG"))

            #print(os.path.join(diretorio, arquivo))