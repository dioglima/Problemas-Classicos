
# Problema do Jantar dos Filósofos e Problema do Leitor/Escritor

Este repositório contém implementações dos famosos problemas de concorrência: o Problema do Jantar dos Filósofos e o Problema do Leitor/Escritor. Esses problemas são comumente usados para ilustrar os desafios de programação concorrente e sincronização em sistemas multitarefa.

## Problema do Jantar dos Filósofos

### Descrição
O Problema do Jantar dos Filósofos é um clássico problema de concorrência que envolve filósofos sentados em uma mesa redonda, cada um com um garfo à esquerda e à direita. Para comer, um filósofo precisa pegar ambos os garfos ao seu lado. No entanto, eles não podem pegar os garfos simultaneamente, o que pode levar a situações de bloqueio se não for implementada uma estratégia adequada.

### Implementação
Neste repositório, você encontrará uma implementação do Problema do Jantar dos Filósofos em Python. A implementação demonstra uma solução para evitar bloqueios, como o algoritmo do garçom ou outras estratégias de sincronização.

## Problema do Leitor/Escritor

### Descrição
O Problema do Leitor/Escritor envolve um recurso compartilhado, como um arquivo ou banco de dados, que pode ser acessado por leitores (que podem apenas ler) e escritores (que podem ler e escrever). O desafio é garantir que os leitores possam acessar o recurso simultaneamente, desde que não haja escritores escrevendo ao mesmo tempo.

### Implementação
Este repositório também inclui uma implementação do Problema do Leitor/Escritor em Python. A implementação demonstra como garantir acesso concorrente seguro para leitores e escritores, evitando condições de corrida e garantindo a integridade dos dados.

## Como Executar
Para executar o código, o primeiro passo é criar um ambiente virtual:

```python -m venv venv```

Ative o ambiente:

```.\venv\Scripts\activate```

Instale as dependências:

```pip install -r requirements.txt```

e execute o código:

```python main.py```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, enviar solicitações de pull e melhorar a implementação.

## Licença
Este projeto é licenciado sob a MIT License.

## Autor
Diogo Lourenço Linhares Lima

