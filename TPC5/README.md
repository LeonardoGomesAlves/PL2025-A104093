# TPC5 - Máquina de Vending

## Data de realização
15/03/2025

## Autor
**Nome:** Leonardo Gomes Alves - A104093

![115940136](https://github.com/user-attachments/assets/68bdbc41-86fd-4a82-91ad-d08d2e9787ac)

## Resumo

### Enunciado do problema
Construir um programa que simule uma máquina de vending.

A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.
```
stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    ...
]
```




### Utilização

#### Input
O programa aceita os seguintes comandos:
- LISTAR - Lista todos os produtos disponíveis com código, nome, quantidade e preço
- MOEDAS <moedas>. - Insere moedas na máquina (1e, 2e, 50c, 20c, 10c, 5c, 2c, 1c)
    - Exemplo: MOEDAS 1e, 50c, 20c.

- SELECIONAR <código> - Seleciona um produto pelo código (formato A##)
    - Exemplo: SELECIONAR A23

- SAIR - Termina a sessão e calcula o trocoInput

#### Implementação
O programa utiliza:

- PLY para a análise léxica dos comandos

- Decimal conseguir calcular com precisão os preços

- JSON para persistência do stock

- Counter para contagem eficiente de moedas no troco
