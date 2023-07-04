# Resolução do problema da mochila com IA
Comparação entre a utilização do algoritmo genético e o recozimento simulado para a resolução do problema

- Algoritmo Genético x Recozimento Simulado
    - 3 itens
    Algoritmo Genético
    ![MochilaIAGen](https://github.com/pauloh-sm/mochila-ia/assets/67742402/574e60c4-ef9f-4a28-8add-7039f4921b0e)
    Recozimento Simulado
    ![MochilaIARS](https://github.com/pauloh-sm/mochila-ia/assets/67742402/7df720d7-a6e0-479b-bbb1-f4ba734524f8)
    - 18 itens
    Algoritmo Genético
    ![image](https://github.com/pauloh-sm/mochila-ia/assets/67742402/7d647638-883b-48af-86ce-3cee6275c612)
    Recozimento Simulado
    ![image](https://github.com/pauloh-sm/mochila-ia/assets/67742402/f660d1a3-7817-4014-bb47-e0a472854393)

Aumentando a quantidade de indivíduos, o algoritmo genético se mostrou mais eficaz, mesmo apresentando um maior tempo para ser executado.

Abaixo algumas execuções contínuas dos dois algoritmos com 20 indivíduos e tamanho máximo suportando de 20 quilos
- Algoritmo Genético
![image](https://github.com/pauloh-sm/mochila-ia/assets/67742402/4dfaba66-9e68-4ca3-a6aa-f79d996b13b9)
- Recozimento Simulado
![image](https://github.com/pauloh-sm/mochila-ia/assets/67742402/24bd75ad-bd6b-4c77-bc8e-a4ceff19c2f2)

# Breve contexto sobre os algoritmos
------------------------------

## Algoritmo Genético:
O algoritmo genético é uma técnica de busca e otimização inspirada no processo de evolução biológica. Ele começa com uma população inicial de soluções (indivíduos) representadas por cromossomos, onde cada cromossomo codifica uma possível solução para o problema em questão. Durante a evolução, os operadores genéticos, como seleção, recombinação (crossover) e mutação, são aplicados para criar novas soluções. A avaliação da qualidade de cada solução é feita por uma função de fitness, que quantifica o quão boa é a solução. As soluções mais aptas têm maior probabilidade de serem selecionadas e reproduzidas, enquanto soluções menos aptas têm menor probabilidade de sobreviver. O algoritmo genético evolui iterativamente, gerando novas gerações de soluções, até atingir um critério de parada, geralmente um número máximo de iterações ou uma condição de convergência.

## Recozimento Simulado:
O recozimento simulado é uma técnica de busca metaheurística que tem como base o processo físico de recozimento de materiais. Ele começa com uma solução inicial e realiza perturbações aleatórias nessa solução. A qualidade da solução perturbada é avaliada por uma função objetivo. O algoritmo aceita mudanças mesmo que piorem a solução atual, com uma probabilidade decrescente ao longo do tempo, permitindo que o algoritmo explore diferentes regiões do espaço de soluções. Essa probabilidade decrescente é inspirada no resfriamento de um material durante o processo de recozimento. A ideia é que, no início, o algoritmo aceite mudanças com maior probabilidade, permitindo a exploração de soluções ruins para evitar ficar preso em mínimos locais. Conforme o tempo passa, a probabilidade de aceitar soluções ruins diminui gradualmente, o que permite ao algoritmo convergir para uma solução ótima.