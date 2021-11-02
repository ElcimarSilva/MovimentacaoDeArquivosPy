import os

lista_arquivos = os.listdir("mover")
lista_arquivos_py = os.listdir("mover/moverPy/")
lista_arquivos_txt = os.listdir("mover/moverTxt/")

def move_dentro_das_pastas():
    for arquivo in lista_arquivos:
        if ".txt" in arquivo:
            os.rename(f"mover/{arquivo}", f"mover/moverTxt/{arquivo}")
        if ".py" in arquivo:
            os.rename(f"mover/{arquivo}", f"mover/moverPy/{arquivo}")
    print ("arquivos movidos para dentro das pastas")

def move_fora_das_pastas():
    for arquivo in lista_arquivos_txt:
        if ".txt" in arquivo:
            os.rename( f"mover/moverTxt/{arquivo}", f"mover/{arquivo}")

    for arquivo in lista_arquivos_py:
        if ".py" in arquivo:
            os.rename(f"mover/moverPy/{arquivo}", f"mover/{arquivo}")
    print ("arquivos movidos para fora das pastas")
 
move_dentro_das_pastas()