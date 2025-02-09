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
            break
        
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

        elif texto[i] == "o" and texto[i:i+2] == "on":
            comportamento = True
            i += 2
        else:
            i += 1
        
    return sum


def main():
    text = "123on12offl=do32on13="
    print(somador(text))
    
if __name__ == "__main__":
    main()