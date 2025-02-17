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
    pattern = r"^([^;]*);([\s\S]*);([^;]*);([^;]*);([^;]*);([^;]*);(O[1-9].*)$"
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
                    objs.append(obj)
                    buffer = ""

            
                    

    return objs

def lista_ordenada_compositores(lista_objs):
    return sorted({obj.compositor for obj in lista_objs})

def print_compositores(lista):
    for comp in lista:
        print(comp)

def n_obras_por_periodo(lista_objs):
    lista = {}

    for obj in lista_objs:
        if obj.periodo not in lista:
            lista[obj.periodo] = 0

        lista[obj.periodo] += 1

    return lista

def print_n_obras_por_periodo(lista):
    for periodo, n in lista.items():
        print(f"Período: {periodo}")
        print(f"  - Nº de obras: {n}")
        print()


def dict_distribuicao_periodo(lista_objs):
    dict = {}

    for obj in lista_objs:
        if obj.periodo not in dict.keys():
            dict[obj.periodo] = []

        dict[obj.periodo].append(obj.nome)

    for obj in dict.keys():
        dict[obj] = sorted(dict[obj])

    return dict

def print_periodo_dict(lista):
    for periodo, nomes in lista.items():
        print(f"Período: {periodo}")
        for nome in nomes:
            print(f"  - {nome}")
        print()


#objs = parser("obras.csv")

#print_compositores(lista_ordenada_compositores(objs))    

#print_periodo_dict(dict_distribuicao_periodo(objs))

#print_n_obras_por_periodo(n_obras_por_periodo(objs))

def main():
    i = "0"
    objs = parser("obras.csv")
    while i != "4":
        print("-------MENU-------")
        print("1 - Lista ordenada alfabeticamente dos compositores musicais")
        print("2 - Distribuição das obras por período: quantas obras catalogadas em cada período")
        print("3 - Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período")
        print("4 - Sair")
        i = input("> ")

        if i == "1":
            print_compositores(lista_ordenada_compositores(objs))  
        elif i == "2":
            print_n_obras_por_periodo(n_obras_por_periodo(objs))
        elif i == "3":
            print_periodo_dict(dict_distribuicao_periodo(objs))
        elif i == "4":
            print("A sair do programa...")
        else:
            print("Input inválido")

        print()

main()