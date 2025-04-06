# Correção Ortográfica com Distância de Levenshtein 

## Descrição do Problema 
A correção ortográfica é um desafio comum em aplicações que envolvem processamento de texto. O objetivo é sugerir palavras corretas para termos digitados incorretamente, baseando-se em um dicionário predefinido. Neste projeto, utilizamos a Distância de Levenshtein para medir a similaridade entre palavras e oferecer sugestões de correção.

## Solução com Programação Dinâmica 
A Distância de Levenshtein mede o número mínimo de operações necessárias para transformar uma palavra em outra. As operações permitidas são: 

- Inserção de um caractere 
- Remoção de um caractere 
- Substituição de um caractere
  
Utilizamos um algoritmo baseado em Programação Dinâmica para calcular essa distância de maneira eficiente. A abordagem reduz a repetição de cálculos intermediários, armazenando valores em uma tabela para reaproveitamento.

## Análise de Complexidade 
Nosso algoritmo tem complexidade de tempo O(m * n), onde m e n são os tamanhos das palavras comparadas. 

- O uso de uma tabela reduz a complexidade da abordagem ingînua recursiva (O(3^m)). 
- Para otimização de espaço, utilizamos apenas duas linhas da tabela, reduzindo a complexidade espacial de O(m * n) para O(n).
  
Para buscas eficientes no dicionário, filtramos palavras de tamanhos próximos ao termo de entrada e ordenamos os resultados por menor distância.

## Escolha do Parâmetro X 
O limite X define a distância máxima aceitável para sugerir palavras semelhantes. 
Escolhemos X = 2 baseado na análise empírica: essa margem cobre a maioria dos erros comuns de digitação sem incluir palavras excessivamente distantes. Esse valor pode ser ajustado conforme o tamanho da palavra: 
- Para palavras curtas (até 4 caracteres), usamos X = 1. 
- Para palavras longas (>10 caracteres), X pode ser aumentado para 3.
  
Essa abordagem balanceia precisão e abrangência nas sugestões. 

## Equipe
<table align="center">
  <tr align="center">
  <td>
      <a href="https://github.com/Caiqueferlima">
        <img src="https://avatars.githubusercontent.com/u/130234796?v=4" width=100 />
        <p>Caíque <br/>Fernandes</p>
      </a>
    </td>
    <td>
      <a href="https://github.com/lukkspereiraa">
        <img src="https://avatars.githubusercontent.com/@lukkspereiraa" width=100 />
        <p>Emilly <br/>Jullyane</p>
      </a>
    </td>
      <a href="https://github.com/Rachelee18">
        <img src="https://avatars.githubusercontent.com/Rachelee18" width=100 />
        <p>Raquel <br/>Medeiros</p>
      </a>
  </tr>
