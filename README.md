# Aplicação para a disciplina de computação distribuida - Ciência da computação

O objetivo deste trabalho é realizar testes de desempenho com duas versões da aplicação Link Extractor, utilizada como exemplo no tutorial Application Containerization and Microservice Orchestration, disponível na plataforma Play-with-Docker. 

A aplicação Link Extractor oferece um front-end web para extrair e exibir todos os links encontrados na página web cujo endereço (URL) é passado como parâmetro. Além do front-end web, desenvolvido em PHP, a arquitetura da aplicação inclui um serviço de extração de links, desenvolvido em duas versões, Python e Ruby, e um serviço de cache, Redis. A figura abaixo ilustra a arquitetura da aplicação Link Extractor na versão em Python.

O serviço de cache é utilizado para acelerar o tempo de extração dos links pelo serviço de extração de link. Quando o serviço de extração de link recebe uma requisição do front-end com uma determinada URL, ele primeiro verifica se os links contidos nessa URL já estão no cache. Se estiverem, o serviço de extração de link retorna ao front-end a lista de links contidas no cache. Do contrário, o serviço de extração de link extrai os links diretamente da URL indicada, armazena os links extraídos no cache, e então retorna a lista de links ao front-end.


# Atividade

Realizar testes de desempenho com as duas versões do serviço de extração de link implementadas em Python e Ruby. Para isso, deve-se utilizar uma ferramenta de teste de carga configurável via script, como Locust ou k6. Implemente o comportamento do usuário virtual a ser criado pela ferramenta de teste de carga de modo a realizar uma sequência de 10 invocações ao serviço de extração de link, passando uma URL diferente como parâmetro a cada invocação. Execute diversos cenários de teste variando: (i) a quantidade de usuários virtuais gerados pela ferramenta de teste de carga; (ii) a versão do serviço de extração de link (Python e Ruby); e (iii) o modo de utilização do serviço de cache (com e sem cache). Armazene as métricas de desempenho coletadas pela ferramenta de teste de carga em cada teste (por exemplo, média, mediana, e percentis do tempo de resposta) em um arquivo ou planilha para posterior análise e visualização.


# Instalação e configuração

## Baixe e instale o python3, docker e docker-compose
- [https://www.python.org/downloads/](https://python-guide-pt-br.readthedocs.io/pt-br/latest/starting/install3/linux.html)
- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

## Configurando ambiente docker-compose

- Entre no linkextractor -> step5(Python) ou linkextractor -> step6(Redis)

- `docker-compose up `

## Configurando ambiente python3

- Entre na raiz do projeto e execute

- `python3 -m venv .venv`

- `source .venv/bin/activate`

- `pip install --upgrade pip`

- `pip install locust`

- `pip install requests`

- `pip install beautifulsoup4`


- `locust -f locustfile.py --csv=results --headless -u 100 --run-time 60`
## Versão automatica (Novo) (Recomendado)
- Agora a nova versão automatica você gera todos os novos arquivos que precisa nos cenarios de testes customizados no código.
- Em vez de rodar algo como `locust -f locustfile.py --csv=results --headless -u 100 --run-time 60`
- Você pode rodar dentro do venv o seguinte comando
- `python3 auto.py -type py --cache`
- `python3 auto.py -type py`
- ou
- `python3 auto.py -type rb --cache`
- `python3 auto.py -type rb`
- Lembre-se de usar o docker-compose do Python quando for a aplicação do python e indicar no -type py
-Lembre-se de usar o docker-compose do Ruby quando for a aplicação do ruby e indicar no -type rb
- Com isso as duas versões serão geradas, 3 casos para o python e 3 casos para o ruby
- As alterações com cache deverão ser feitas na mão! (Por enquanto)

## Aplicações
- Locust: http://localhost:8089


## Equipe
- Erick Bernardo
- Marcelo Barbosa
- Leonardo Pontes

## Ferramenta utilizada: Locust

- Uma ferramenta de teste de carga de código aberto.
- Defina o comportamento do usuário com código Python e enxameie seu sistema com milhões de usuários simultâneos.
- Defina o comportamento do usuário no código
Não há necessidade de UIs desajeitadas ou XML inchado. Apenas código simples.
- Distribuído e escalável
O Locust suporta a execução de testes de carga distribuídos em diversas máquinas e, portanto, pode ser usado para simular milhões de usuários simultâneos.
- Comprovado e testado em batalha
Locust tem sido usado para simular milhões de usuários simultâneos. Battlelog, o aplicativo da web para os jogos Battlefield, é testado em carga usando o Locust, então pode-se realmente dizer que o Locust é testado em batalha;).

## Cenários de testes
- Para todos os cenários foram usados as seguintes URLS, no tempo de 3 min de duração:
```python
    urls_to_extract = [
        "https://brazino777.com/pt/",
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
    ]
```
- A variação do spawn rate se deu em consideração a quantidade de usuários para que o máximo de usuários fosse atingido rapidamente sem afetar muito o indice de falhas, baseado na maquina usada.

1) Primeiro cenário: 100 usuários com spawn rate de 10
 
- Comando utilizado:
- `locust -f locustfile.py --csv=results --headless -u 100 -r 10 --run-time 180`


