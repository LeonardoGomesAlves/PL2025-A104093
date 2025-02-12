import re
import sys

def somador(texto: str):
    i = 0
    sum = 0
    val = 0
    comportamento = False
    texto = texto.lower()

    while i < len(texto):
        if texto[i] == "=":
            print(f"{sum}")
            i += 1
        
        elif comportamento:
            if texto[i] == "o" and texto[i:i+3] == "off":
                comportamento = False
                i += 3
            
            elif texto[i].isdigit(): #verifica se é um número
                while i < len(texto) and texto[i].isdigit():
                    val = val * 10 + int(texto[i])
                    i += 1
                sum += val
                val = 0

            else: 
                i += 1

        elif texto[i] == "o" and texto[i:i+2] == "on":
            comportamento = True
            i += 2
        else:
            i += 1

def main():
    file = sys.argv[1]

    with open(file) as f:
        text = f.read()

    somador(text)
    

main()