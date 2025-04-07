# Correção Ortográfica com Distância de Levenshtein 

## Índice

1. [Descrição do Problema](#descrição-do-problema)
2. [Solução com Programação Dinâmica](#solução-com-programação-dinâmica)
3. [Análise de Complexidade](#analise-de-complexidade)
4. [Escolha do Parâmetro X](#Escolha-do-Parâmetro-X)
5. [Conclusão](#Conclusao)
6. [Equipe](#Equipe)

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
Escolhemos X = 2 baseado na análise empírica: essa margem cobre a maioria dos erros comuns de digitação sem incluir palavras excessivamente distantes.

- Um valor pequeno como 1 pode ser restritivo demais (exclui palavras parecidas com 2 erros de digitação).
- Um valor grande como 3 ou mais pode gerar muitas sugestões irrelevantes.
- O valor 2 representa um bom equilíbrio: considera erros comuns (como trocar duas letras, esquecer uma letra ou digitar uma letra errada) e ainda mantém o desempenho razoável, especialmente para dicionários grandes.
  
Essa abordagem balanceia precisão e abrangência nas sugestões. 

## Conclusão 
O sistema implementado proporciona sugestões de correção eficientes e escaláveis. A otimização da memória e a seleção inteligente de candidatos tornam o algoritmo prático para aplicações reais, como corretores ortográficos e assistentes de texto. 

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
        <img src="https://avatars.githubusercontent.com/lukkspereiraa" width=100 />
        <p>Lucas <br/>Pereira</p>
      </a>
    </td>
    <td>
      <a href="https://github.com/Rachelee18">
        <img src="https://avatars.githubusercontent.com/Rachelee18" width=100 />
        <p>Raquel <br/>Medeiros</p>
      </a>
    </td>
