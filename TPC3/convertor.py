import re
import sys

def cabecalho_regex(linha):
    m = re.match(r"^\s*(#{1,6})\s+(.*)$", linha)

    if m:
        header = len(m.group(1))
        linha = f"<h{header}>{m.group(2)}</h{header}>"

    return linha

def bold_regex(linha):
    return re.sub(r"\*\*([^\s].*?)\*\*", f"<b>\1</b>", linha)

def italico_regex(linha):
    return re.sub(r"\*([^\s].*?)\*", f"<i>\1</i>", linha)

def lista_numerada_regex(linha):
    pass

def url_regex(linha):
    return re.sub(r"\[(.*)\]\((.*)\)", r'<a href="\2">\1</a>', linha) 

def image_regex(linha):
    return re.sub(r"!\[(.*)\]\((.*)\)", r'<img src="\2" alt="\1"/>', linha)

def convertor(file):
    texto = ""
    with open(file, "r", encoding="utf-8") as f:
        texto = f.read()

    lines = texto.split('\n')

    for linha in lines:
        linha = cabecalho_regex(linha)
        linha = bold_regex(linha)
        linha = italico_regex(linha)
        linha = image_regex(linha)
        linha = url_regex(linha)
        
        print(linha)
        


def main(args):
    if len(args) > 1:
        convertor(args[1])


if __name__ == "__main__":
    main(sys.argv)