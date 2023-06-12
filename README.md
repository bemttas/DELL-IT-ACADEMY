# Processo Seletivo It Academy

Este repositório contém o código desenvolvido como parte do teste de entrada para o Dell IT Academy. O objetivo deste teste é avaliar as habilidades e conhecimentos técnicos do candidato em relação à programação em Python e resolução de problemas computacionais.

## Descrição do código

O código consiste em uma calculadora de rotas e custos de transporte, implementada em Python. Ele lê informações de arquivos CSV que contêm dados sobre cidades, distâncias, caminhões, itens e seus respectivos pesos e preços. Com base nesses dados, o programa calcula as rotas mais eficientes e os custos de transporte correspondentes.

## Uso

Para utilizar o código, siga as instruções abaixo:

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório em sua máquina local.
3. Navegue até o diretório onde o repositório foi clonado.
4. Certifique-se de ter os arquivos CSV necessários (`DNIT-Distancias.csv`, `Caminhoes.csv` e `Itens.csv`) presentes no diretório.
5. Execute o arquivo `main.py` em um ambiente Python.
6. Siga as instruções exibidas na interface do programa para interagir com ele e obter os resultados desejados.

## Pré-requisitos

- Python 3.5 ou superior
- Biblioteca CSV

## Arquivos de entrada

O programa utiliza três arquivos CSV para funcionar corretamente:

1. `DNIT-Distancias.csv`: Contém informações sobre as distâncias entre as cidades.
2. `Caminhoes.csv`: Contém informações sobre os tipos de caminhões disponíveis, seus pesos máximos e preços de transporte.
3. `Itens.csv`: Contém informações sobre os itens a serem transportados.

Certifique-se de fornecer esses arquivos corretamente antes de executar o programa.

## Estrutura do código

O código segue a seguinte estrutura:

1. Abertura do arquivo `DNIT-Distancias.csv` para obter informações sobre as distâncias entre as cidades.
2. Leitura das cidades da primeira linha do arquivo e armazenamento em uma lista chamada `cidades`.
3. Armazenamento das distâncias em uma matriz chamada `distancias`.
4. Abertura do arquivo `Caminhoes.csv` para obter informações sobre os caminhões disponíveis.
5. Leitura das informações de cada caminhão, como peso máximo e preço, e armazenamento em listas separadas.
6. Leitura das informações sobre os itens a serem transportados a partir do arquivo `Itens.csv` e armazenamento em listas.
7. Criação de uma matriz vazia chamada `rotas` para armazenar as rotas que serão cadastradas.

## Contribuição

Este repositório destina-se apenas ao envio do teste para avaliação no Dell IT Academy.
