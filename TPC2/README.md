# TPC2 - Análise de um dataset de obras musicais

## Data de realização
12/02/2024

## Autor
**Nome:** Leonardo Gomes Alves - A104093

![115940136](https://github.com/user-attachments/assets/68bdbc41-86fd-4a82-91ad-d08d2e9787ac)

## Resumo

### Enunciado do problema
- Neste TPC, é proibido usar o módulo CSV do Python;
- Deverás ler o dataset, processá-lo e criar os seguintes resultados:

  1. Lista ordenada alfabeticamente dos compositores musicais;
  2. Distribuição das obras por período: quantas obras catalogadas em cada período;
  3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.

### Interpretação do problema

Dado o problema, é necessário numa primeira fase ler o ficheiro **csv** onde, cada linha, representa uma obra musical juntamente com alguns atributos, separados por ponto e vírgula.

Como não é permitido a utilização do módulo csv, comecei por determinar uma expressão regular que fosse capaz de interpretar corretamente as linhas csv.

Desta forma, após feita a leitura correta do ficheiro, bastaria desenvolver o código necessário para implementar as queries pedidas.

### Implementação
A implementação foi feita no ficheiro <a href="https://github.com/LeonardoGomesAlves/PL2025-A104093/blob/main/TPC2/parser.py">**parser.py**</a>, que implementa a solução do problema da seguinte forma:

  1. Leitura das linha csv

     - Vai lendo linha a linha, armazenando temporariamente cada uma num buffer, até que contenha uma linha completa que respeite a expressão regular;
     - São extraidas, cada uma das variáveis do objeto, através da expressão regular, criando assim um objeto, que representa cada obra, e guardando-o numa lista.

  3. Processamento das queries

     - A função `lista_ordenada_compositores` é responsável por extrair os nomes dos compositores e ordená-los alfabeticamente, utilizando um set para não aparecerem nomes repetidos;
     - A função `n_obras_por_periodo` percorre a lista de objetos e conta quantas obras existem de um determinado período;
     - A função `dict_distribuicao_periodo` cria um dicionário, organizado por períodos, onde cada um tem a si associado uma lista das obras desse mesmo período;
  
  5. Interface do utilizador

     - Cada uma das funções mencionadas no ponto anterior têm a si associada uma função responsável por imprimir as informações relativas a essa query.


## Conclusão

Por fim, o programa desenvolvido fazer o parsing das linhas csv, utilizando expressões regulares, que nos permitem assim, executar as queries propostas no enunciado do trabalho.
