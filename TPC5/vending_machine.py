import ply.lex as lex
from datetime import datetime
from collections import Counter
import json
from decimal import Decimal, ROUND_HALF_UP

global saldo
saldo = Decimal('0.00')

global stock

with open('stock.json', 'r') as r:
    stock = json.load(r)

tokens = (
    'OPERACAO',
    'MOEDA',
    'PRODUTO',
    'VIRGULA',
    'PONTO'
)

t_OPERACAO = r'\b[A-Z]+\b'
t_PRODUTO = r'A\d\d'
t_VIRGULA = r','
t_PONTO = r'\.'

def t_MOEDA(t):
    r'1e|2e|50c|20c|10c|5c|2c|1c'
    return t

def initialize():
    print(f"maq: {datetime.now().date()}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido")

def operacao_listar():
    print("maq:")
    print("cod   |  nome     | quantidade |  preço")
    for product in stock:
        print(f"{product['cod']}   |  {product['nome']} | {product['quant']} | {product['preco']}")

def processar_moeda(moeda: str):
    global saldo
    if moeda.endswith('e'):
        saldo += Decimal(moeda.split('e')[0])
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    else:
        saldo += Decimal(moeda.split('c')[0]) * Decimal('0.01')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def processar_produto(produto: str):
    global stock, saldo
    for product in stock:
        if product['cod'] == produto:
            if product['quant'] > 0:
                if saldo >= Decimal(str(product['preco'])):
                    saldo -= Decimal(str(product['preco']))
                    saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    product['quant'] -= 1
                    print(f"maq: Pode retirar o produto dispensado \"{product['nome']}\"")
                    print(f"maq: Saldo = {saldo}e")
                    return
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo}e; Pedido = {product['preco']}e")
                    return
            else:
                print(f"maq: O produto selecionado,{produto}, não possui stock")
                return
    print(f"maq: O produto selecionado,{produto}, não existe")


def calcular_troco():
    global saldo
    moedas = []
    saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    while saldo >= Decimal('2.00'):
        moedas.append("2e")
        saldo -= Decimal('2.00')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('1.00'):
        moedas.append("1e")
        saldo -= Decimal('1.00')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('0.50'):
        moedas.append("50c")
        saldo -= Decimal('0.50')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('0.20'):
        moedas.append("20c")
        saldo -= Decimal('0.20')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('0.10'):
        moedas.append("10c")
        saldo -= Decimal('0.10')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('0.05'):
        moedas.append("5c")
        saldo -= Decimal('0.05')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    while saldo >= Decimal('0.01'):
        moedas.append("1c")
        saldo -= Decimal('0.01')
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    if len(moedas) > 0:
        n_moedas = Counter(moedas)

        moedas_formatadas = [f"{quantidade}x {moeda}" for moeda, quantidade in sorted(n_moedas.items())]

        print("Pode retirar o troco: " + ", ".join(moedas_formatadas))

    print("maq: Até à próxima")

def main():
    initialize()
    while True:
        lexer.input(input('>> '))
        tok = lexer.token()
        if not tok:
            break
        if tok.type == "OPERACAO":
            if tok.value == "LISTAR":
                operacao_listar()

            elif tok.value == "MOEDAS":
                while True:
                    tok = lexer.token()
                    if not tok:
                        break
                    if tok.type == "PONTO":
                        break
                    elif tok.type == "VIRGULA":
                        continue
                    elif tok.type == "MOEDA":
                        processar_moeda(tok.value)

            elif tok.value == "SELECIONAR":
                tok = lexer.token()
                if not tok:
                    break
                if tok.type == "PRODUTO":
                    processar_produto(tok.value)

            elif tok.value == "SAIR":
                calcular_troco()
                break

    with open('stock.json', 'w') as w:
        json.dump(stock, w, ensure_ascii=False)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = r' \t'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

main()
