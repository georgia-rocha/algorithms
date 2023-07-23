# Boas Vindas ao Repositório do Projeto Algorithms

Este projeto implementei alguns dos principais algoritmos de busca e ordenação com Python, com o intuito de resolver e otimizar algoritmos. Os algoritmos foram implementados do zero, sem o uso de bibliotecas externas, para solucionar diversos problemas propostos.

<details><summary> Para Clonar e Testar a Aplicação</summary>
<br>

1. Para clonar a aplicação:

```
git clone git@github.com:georgia-rocha/algorithms.git
```

2. Para entrar no diretório do projeto:
```
 cd algorithms
```

3.  Para criar um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Executar os testes:
```
python3 -m pytest
```
O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nome_do_arquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

```bash
python -m pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
python -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>


## Requisitos 100%

<details><summary>1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca):</summary>
  <ul>
    <li>O código foi feito dentro do arquivo challenges/challenge_study_schedule.py.</li>
    <li>É verificado pelo avaliador se:</li>
  </ul> 
  <ol>
    <li> Retorna a quantidade de estudantes presentes para uma entrada específica;</li>
    <li>Retorna None se em permanence_period houver alguma entrada inválida;</li>
    <li>Retorna None se target_time recebe um valor vazio;</li>
    <li>A função se comporta como no máximo O(n), ou seja, com complexidade assintótica linear.</li>
  </ol>
</details>
<details><summary>2 - Criptografia de inversões (Testes)</summary>
<ul>
  <li>Esse teste se chama test_encrypt_message, e ele garante que a função de criptografia encrypt_message respeitar uma lógica específica</li>
</ul>
<ol>
  <li>O teste rejeita implementações que invertem a lógica de "par ou ímpar";</li>
  <li>O teste rejeita implementações que não aplicam a regra de índice positivo válido;</li>
  <li>O teste rejeita implementações que aplicam ordenação ao invés de inversão;</li>
  <li>O teste rejeita implementações que não validam o tipo das entradas;</li>
  <li>O teste aprova implementações corretas.</li>
</ol>
</details>
<details><summary>3 - Palíndromos (Recursividade)</summary>
<ul>
  <li>O código foi feito dentro do arquivo challenges/challenge_palindromes_recursive.py.</li>
</ul>
<ol>
  <li>Retorna True se a palavra passada por parâmetro for um palíndromo;</li>
  <li>Retorna False se a palavra passada por parâmetro não for um palíndromo;</li>
  <li>Retorna False se nenhuma palavra for passada por parâmetro.</li>
</ol>
</details>
<details><summary>4 - Anagramas (Algoritmo de ordenação)</summary>
<ul>
  <li>O código foi feito dentro do arquivo challenges/challenge_anagrams.py.</li>
</ul>
<ol>
  <li>Retorna True se as palavras passadas por parâmetro forem anagramas;</li>
  <li>Retorna False se as palavras passadas por parâmetro não forem anagramas;</li>
  <li> Retorna False se alguma das palavras passadas por parâmetro for uma string vazia;</li>
  <li>A função se comporta como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica.</li>
  <li>Retorna True se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas.</li>
</ol>
</details>
<details><summary>5 - Encontrando números repetidos (Algoritmo de busca)</summary>
<ul>
  <li>O código foi feito dentro do arquivo challenge_find_the_duplicate.py.</li>
</ul>
<ol>
  <li>Retorna o númaro repetido se a função receber como parâmetro uma lista com números repetidos;</li>
  <li>Retorna False se a função não receber nenhum parâmetro;</li>
  <li>Retorna False se a função receber como parâmetro uma string;</li>
  <li>Retorna False se a função receber como parâmetro uma lista sem números repetidos;</li>
  <li>Retorna False se a função receber como parâmetro apenas um valor;</li>
  <li>Retorna False se a função receber como parâmetro um número negativo;</li>
  <li>A função se comporta como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica.</li>
</ol>
</details>
<details><summary>6 - Palíndromos (Iteratividade)</summary>
<ul>
  <li>O código foi feito dentro do arquivo challenge_palindromes_iterative.py.</li>
</ul>
<ol>
  <li>Retorna True se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa;</li>
  <li>Retorna False se a palavra passada como parâmetro não for um palíndromo, executando uma função iterativa;</li>
  <li>Retorna False se nenhuma palavra for passada como parâmetro, executando uma função iterativa ;</li>
  <li>A função se comporta como no máximo O(n), ou seja, com complexidade assintótica linear.</li>
</ol>
</details>
