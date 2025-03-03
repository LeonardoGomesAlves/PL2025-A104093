import re
import sys

def cabecalho_regex(linha):
    m = re.match(r"^\s*(#{1,6})\s+(.*)$", linha)

    if m:
        header = len(m.group(1))
        linha = f"<h{header}>{m.group(2)}</h{header}>"

    return linha

def bold_regex(linha):
    return re.sub(r"\*\*([^\s].*?)\*\*", r"<b>\1</b>", linha)

def italico_regex(linha):
    return re.sub(r"\*([^\s].*?)\*", r"<i>\1</i>", linha)

def lista_numerada_regex(linha):
    pass

def url_regex(linha):
    return re.sub(r"\[(.*)\]\((.*)\)", r'<a href="\2">\1</a>', linha) 

def image_regex(linha):
    return re.sub(r"!\[(.*)\]\((.*)\)", r'<img src="\2" alt="\1"/>', linha)

def lista_numerada_regex(linhas):
    list_regex = r"^(\d+)\.\s([^\n]*)"
    resultado = []
    inside_list = False

    for linha in linhas:
        if re.match(list_regex, linha):
            if not inside_list:
                resultado.append("<ol>")
                inside_list = True
            resultado.append(re.sub(list_regex, r'<li>\2</li>', linha))
        else:
            if inside_list:
                resultado.append("</ol>")
                inside_list = False
            resultado.append(linha)

    if inside_list:
        resultado.append("</ol>")

    return resultado
                


def convertor(file: str):
    html = ""
    with open(file, "r", encoding="utf-8") as f:
        texto = f.read().split('\n')

    lines = lista_numerada_regex(texto)

    for i in range(len(lines)):
        lines[i] = cabecalho_regex(lines[i])
        lines[i] = bold_regex(lines[i])
        lines[i] = italico_regex(lines[i])
        lines[i] = image_regex(lines[i])
        lines[i] = url_regex(lines[i])
        
        html = "\n".join(lines)

    file_name = file.split('.')
    with open(file_name[0] + ".html", "w", encoding="utf-8") as w:
        w.write(html)
    
# Usage: python3 convertor.py <file.md>
def main(args):
    if len(args) > 1:
        convertor(args[1])


if __name__ == "__main__":
    main(sys.argv)