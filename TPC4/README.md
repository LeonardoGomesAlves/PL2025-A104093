# TPC3 - Analisador Léxico

## Data de realização
15/03/2025

## Autor
**Nome:** Leonardo Gomes Alves - A104093

![115940136](https://github.com/user-attachments/assets/68bdbc41-86fd-4a82-91ad-d08d2e9787ac)

## Resumo

### Enunciado do problema
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Tokens
'COMMENT',
'SELECT',
'VAR',
'WHERE',
'CE',
'CD',
'POINT',
'ID',
'TYPE',
'LIMIT',
'WORD'

### Utilização

#### Input
```
# DBPedia: obras de Chuck Berry
    select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Output
```
LexToken(COMMENT,'DBPedia: obras de Chuck Berry',2,1)
LexToken(SELECT,'select',4,38)
LexToken(VAR,'?nome',4,45)
LexToken(VAR,'?desc',4,51)
LexToken(WHERE,'where',4,57)
LexToken(CE,'{',4,63)
LexToken(VAR,'?s',5,69)
LexToken(WORD,'a',5,72)
LexToken(TYPE,'dbo:MusicalArtist',5,74)
LexToken(POINT,'.',5,91)
LexToken(VAR,'?s',6,97)
LexToken(TYPE,'foaf:name',6,100)
LexToken(ID,'"Chuck Berry"@en ',6,110)
LexToken(POINT,'.',6,127)
LexToken(VAR,'?w',7,133)
LexToken(TYPE,'dbo:artist',7,136)
LexToken(VAR,'?s',7,147)
LexToken(POINT,'.',7,149)
LexToken(VAR,'?w',8,155)
LexToken(TYPE,'foaf:name',8,158)
LexToken(VAR,'?nome',8,168)
LexToken(POINT,'.',8,173)
LexToken(VAR,'?w',9,179)
LexToken(TYPE,'dbo:abstract',9,182)
LexToken(VAR,'?desc',9,195)
LexToken(CD,'}',10,201)
LexToken(LIMIT,'1000',10,203)
```
