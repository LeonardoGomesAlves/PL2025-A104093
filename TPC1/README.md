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

### Exemplo da compilação do programa
<pre>
python3 somador.py input.txt
</pre>

**input.txt** - ficheiro que possuirá o texto;

### Implementação
O programa desenvolvido, **somador.py**, implementa o somador baseado na minha interpretação do problema.

Para tal, utilizei as seguintes variáveis:
- **i** - indíce do loop que percorre a string;
- **sum** - acumula a soma dos valores encontrados;
- **val** - variável temporário que auxilia a construir os números encontrados no texto;
- **comportamento** - variável booleana que indica se o comportamento da soma está ativado ou desativado.

Assim, quando aparece, por exemplo, a string "On" no texto, a variável **comportamento** é alterada para **True** e os valores que aparecerem daí em diante, enquanto não aparecer a string "Off", são calculados em **val** (auxilia a construção em números com mais do que um dígito) e adiciona-o na variável **sum**. Assim, quando aparecer o caráter "=",  o valor em **sum** é apresentado no terminal do utilizador. 
