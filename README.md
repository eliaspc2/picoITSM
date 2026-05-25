# picoITSM

Sistema simples de gestão de infraestruturas e incidentes (ITSM), desenvolvido em Python com interface por linha de comandos.

## Objetivo do projeto

Este projeto foi desenvolvido no âmbito da UFCD 10790 - Projeto de Programação, do curso EFA Programador/a de Informática.

O principal objetivo é aplicar conhecimentos adquiridos ao longo do curso, incluindo:

* programação em Python
* bases de dados SQLite
* modelação de dados
* algoritmos
* estruturas de dados
* organização de software
* controlo de versões com Git

O objetivo académico do projeto é cumprir os requisitos da UFCD e obter aprovação na mesma.

## Formador

* Nuno Carapito
* Empresa: Tecnisign

## Tecnologias utilizadas

* Python
* SQLite
* Git/GitHub
* Visual Studio Code

## Tipo de aplicação

Aplicação totalmente desenvolvida em linha de comandos (CLI).

## Funcionalidades previstas

* Criar técnicos
* Criar competências
* Associar competências a técnicos
* Criar tickets
* Atribuir tickets automaticamente
* Atualizar estado dos tickets
* Consultar tickets
* Persistência de dados em SQLite

## Algoritmo principal

O sistema irá atribuir tickets automaticamente com base em:

* competências do técnico
* carga de trabalho atual
* disponibilidade

## Estrutura inicial do projeto

```text
picoITSM/
│
├── docs/
├── database/
├── src/
│   └── main.py
│
├── README.md
└── requirements.txt
```

# Roadmap do Projeto

## Entrega 1 - Análise do problema e requisitos

* Definição do stack tecnológico
* Documento de requisitos funcionais e não-funcionais
* Diagrama Entidade-Relacionamento
* Diagrama de Classes
* Inicialização do repositório Git

## Entrega 2 - Modelação e desenho do sistema

* Criação da base de dados SQLite
* Implementação das entidades
* Operações CRUD básicas
* Dados de teste (seeding)

## Entrega 3 - Infraestrutura e base técnica

* Estruturas de dados em memória
* Implementação do algoritmo principal
* Organização por camadas
* Comunicação entre módulos

## Entrega 4 - Implementação funcional principal

* Funcionalidades principais completas
* Menus por consola
* Persistência de dados funcional
* Validação e tratamento de erros

## Entrega 5 - Segurança, testes e fiabilidade

* Autenticação simples
* Tratamento de exceções
* Logs básicos
* Testes unitários
* Verificação de vulnerabilidades

## Entrega 6 - Otimização, documentação e defesa

* Otimizações finais
* Documentação técnica
* Manual de utilização
* Preparação da apresentação final
