# TPC1 - Somador on/off

## Data de realização
12/02/2024

## Autor
**Nome:** Leonardo Gomes Alves - A104093

![115940136](https://github.com/user-attachments/assets/68bdbc41-86fd-4a82-91ad-d08d2e9787ac)

## Resumo

### Enunciado do problema

  1. Pretende-se um programa que some todas as sequências de dígitos que encontra num texto;
  2. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
  3. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
  4. Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.

### Interpretação do problema

Dado o problema, considerei que o comportamento da soma iniciaria desligado, desta forma, para que os números começem a ser somados é necessário aparecer a string "On".
Sempre que aparece a string "Off", o comportamento da soma é desligado, ou seja, os próximos números que aparecerem imediatamente, que não precedam a string "On", não serão somados.
Quando aparecer o caráter "=", o valor da soma nesse momento é escrito no ecrã.

### Exemplo

**Input**
<pre>
123on122asdoffl=do32on13=of344=?off4333=
</pre>

**Output**
```
122
135
479
479
```

### Exemplo da compilação do programa:
<pre>
python3 somador.py input.txt
</pre>

**input.txt** - ficheiro que possuirá o texto;

