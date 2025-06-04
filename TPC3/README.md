# TPC3 - Conversor MarkDown para HTML

## Data de realização
03/03/2025

## Autor
**Nome:** Leonardo Gomes Alves - A104093

![115940136](https://github.com/user-attachments/assets/68bdbc41-86fd-4a82-91ad-d08d2e9787ac)

## Resumo

### Enunciado do problema
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic
Syntax" da Cheat Sheet.

### Implementação
A implementação foi feita no ficheiro <a href="https://github.com/LeonardoGomesAlves/PL2025-A104093/blob/main/TPC3/convertor.py">**convertor.py**</a>, que implementa a solução do problema da seguinte forma:

1. Para conseguir transformar os cabeçalhos, bold, itálico, url e imagens de MarkDown para HTML utilizei as seguintes expressões regulares, juntamente com a função sub da biblioteca re de python, onde substituei os campos necessários por código HTML:

   - Cabeçalho: ```^\s*(#{1,6})\s+(.*)$```
   - Bold: ```\*\*([^\s].*?)\*\*```
   - Itálico: ```\*([^\s].*?)\*```
   - Url: ```\[(.*)\]\((.*)\)```
   - Imagem: ```!\[(.*)\]\((.*)\)```

2. Assim, falta desenvolver uma função que seja responsável por traduzir as listas numeradas. Para tal, desenvolvi a função `lista_numerada_regex`, em que utiliza a expressão regular ```^(\d+)\.\s([^\n]*)```, para conseguir obter o padrão de uma lista numerada em MarkDown.
Desta forma, basta percorrer todas as linhas do ficheiro e, enquanto houverem linhas seguidas que sigam essa expressão regular, estas vão sendo transformadas para HTML.
  
3. Desenvolvidas então as funções que transformam linhas MarkDown para HTML (por exemplo, `cabecalho_regex`), basta aplicar-mos cada uma destas a cada uma das linhas presentes no ficheiro MarkDown que é passado como argumento e será então gerado um novo ficheiro, como o mesmo nome, sendo apenas do tipo HTML.

## Conclusão

Por fim, o programa desenvolvido faz todas as funcionalidades descritas no enunciado, o que permite a tradução correta dum ficheiro MarkDown para um HTML.
