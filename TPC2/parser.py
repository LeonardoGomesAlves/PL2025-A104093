import re
import csv

class Objeto:
    def __init__(self, nome, desc, anoCriacao, periodo, compositor, duracao, id):
        self.nome = nome
        self.desc = desc
        self.anoCriacao = anoCriacao
        self.periodo = periodo
        self.compositor = compositor
        self.duracao = duracao
        self.id = id

# nome;desc;anoCriacao;periodo;compositor;duracao;_id

def parser(file_path: str):
    pattern = r"^([^;]*);([\s\S]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*)$"
    objs = []
    buffer = ""

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        i = 0
        for line in f:
            buffer += line.strip() + " "

            if buffer.count(";") >= 6:
                buffer.strip()
                match = re.match(pattern, buffer)
                if match:
                    obj = Objeto(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6), match.group(7))
                    if obj.compositor == "1417":
                        print(buffer + "\n\n")
                    objs.append(obj)
                    buffer = ""

            
                    

    return objs

def lista_ordenada(lista_objs):
    lista_nomes = {obj.compositor for obj in lista_objs}
    lista_ord = sorted(lista_nomes)
    #print(len(lista_nomes))
    for o in lista_ord:
        print(o)



objs = parser("obras.csv")

lista_ordenada(objs)


            

