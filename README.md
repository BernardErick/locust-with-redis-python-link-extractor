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

## Aplicações
- Locust: http://localhost:8089