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

## Utilizadores de teste

Depois de executar o seed da base de dados, existem dois utilizadores principais para teste:

```text
admin - admin123
user  - user123
```

O utilizador `admin` tem perfil `ADMIN`.
O utilizador `user` tem perfil `TECNICO`.

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

# Estado por Entrega

## Entrega 1 - Análise do problema e requisitos

Na Entrega 1 ficou preparada a base documental e organizacional do projeto.

Ficou pronto:

* Definição do stack tecnológico em `docs/01_stack_tecnologico.md`
* Documento de requisitos funcionais e não-funcionais em `docs/02_requisitos.md`
* Diagrama Entidade-Relacionamento em `docs/03_diagrama_entidade_relacionamento.md`
* Diagrama de Classes em `docs/04_diagrama_classes.md`
* Documentação do repositório e scaffold em `docs/05_repositorio_e_scaffold.md`
* Guia do código, objetos públicos e ficheiros em `docs/06_guia_codigo_e_objetos.md`
* Repositório Git inicializado
* Repositório alojado no GitHub
* Estrutura inicial de pastas do projeto
* README inicial com descrição, objetivo, tecnologias e roadmap
* Matriz de requisitos com identificação, prioridade e estado de implementação
* Diagramas Mermaid atualizados e coerentes com o código
* Modelação das funcionalidades completas previstas no enunciado

Estado da entrega: concluída a 100%.

Nota: a análise identifica o inventário de ativos e a disponibilidade horária
como requisitos do âmbito completo. Estas funcionalidades estão corretamente
modeladas, mas a sua implementação pertence às entregas técnicas posteriores.

## Entrega 2 - Modelação e desenho do sistema

Na Entrega 2 ficou implementada a base técnica de persistência e modelação do domínio.

Ficou pronto:

* Criação da base de dados SQLite
* Script de criação das tabelas em `src/database/init_db.py`
* Ligação à base de dados em `src/database/db_connection.py`
* Script de dados de teste em `src/database/seed_db.py`
* Modelos de domínio:
  * `Utilizador`
  * `Tecnico`
  * `Cliente`
  * `Competencia`
  * `Ticket`
* Repositórios com operações CRUD básicas:
  * `UtilizadorRepository`
  * `TecnicoRepository`
  * `ClienteRepository`
  * `CompetenciaRepository`
  * `TicketRepository`
* Persistência de dados em SQLite
* Criação da tabela de relação `tecnico_competencia`
* Inserção de dados iniciais para testar técnicos, clientes, competências, utilizadores e tickets

Estado da entrega: concluída.

## Entrega 3 - Infraestrutura e base técnica

Na Entrega 3 ficou implementada a infraestrutura em memória, a comunicação entre camadas e o algoritmo principal de atribuição automática.

Ficou pronto:

* Classe `MemoryCache` em `src/services/memory_cache.py`
* Estruturas de dados em memória carregadas a partir da BD
* Estrutura única `dados` partilhada entre módulos
* Carregamento da tabela `tecnico_competencia`
* Serviço `TicketService` em `src/services/ticket_service.py`
* Algoritmo para escolher técnico elegível
* Matching entre competência do ticket e competências do técnico
* Cálculo de carga de trabalho por técnico
* Exclusão de tickets com estado `FECHADO` no cálculo da carga
* Utilização de Heap/Priority Queue com `heapq`
* Integração inicial entre `main.py`, `Menu`, `MemoryCache`, `TicketService`, repositórios e SQLite
* Criação de tickets através do menu com atribuição automática
* Recarregamento automático da cache após criar ticket
* Testes unitários do algoritmo em `src/tests/test_ticket_service.py`

### Arquitetura da Entrega 3

As estruturas de dados em memória são carregadas a partir da base de dados SQLite através da classe `MemoryCache`.

Estruturas em memória:

* utilizadores
* tecnicos
* clientes
* competencias
* tecnico_competencia
* tickets

Fluxo entre camadas:

```text
Menu
↓
Service
↓
MemoryCache
↓
Repository
↓
SQLite
```

O algoritmo de atribuição automática utiliza uma Heap (Priority Queue), implementada através do módulo `heapq`, para selecionar o técnico elegível com menor carga de trabalho.

O fluxo da atribuição automática é:

```text
BD
↓
Memória
↓
Algoritmo
↓
Atualização
```

Depois de criar um ticket com `ticket_service.criar_ticket_com_atribuicao(...)`, a cache é recarregada com `cache.recarregar()`, mantendo os dados em memória sincronizados com a base de dados.

Testes implementados:

* técnico com competência é escolhido
* técnico com menor carga é escolhido
* sem candidatos retorna `None`

Comando para executar os testes:

```bash
python -m unittest discover -s src/tests
```

### Como testar a Entrega 3

Para preparar a base de dados com dados de teste:

```bash
python src/database/seed_db.py
```

Para executar os testes do algoritmo:

```bash
python -m unittest discover -s src/tests
```

Para iniciar a aplicação e testar os menus:

```bash
python src/main.py
```

Estado da entrega: concluída.

## Entrega 4 - Implementação funcional principal

Na Entrega 4 ficou implementada a parte funcional principal da aplicação através da interface por consola.

Ficou pronto:

* Menu principal por perfil de utilizador
* Menu de clientes com criação, listagem, edição e remoção
* Menu de tickets com criação, listagem, edição e remoção
* Alteração de estado de tickets
* Fecho de tickets
* Menu de técnicos restrito a administradores
* Criação, listagem, edição e remoção de técnicos
* Criação automática de utilizador da aplicação ao criar técnico
* Menu de competências restrito a administradores
* Criação, listagem, edição e remoção de competências
* Associação de competências a técnicos
* Remoção de competências associadas a técnicos
* Menu de utilizadores restrito a administradores
* Criação de utilizadores `ADMIN` e `TECNICO`
* Listagem, edição e remoção de utilizadores
* Validação de campos obrigatórios
* Validação de email
* Validação de prioridade e estado de tickets
* Validação de IDs existentes antes de operações
* Bloqueio de remoções que quebrariam relações existentes
* Persistência funcional em SQLite
* Recarregamento da cache após alterações

Estado da entrega: concluída.

### API interna da aplicação

Como o projeto é uma aplicação CLI, não foi implementada uma API HTTP. A API funcional do projeto é a camada interna de classes, organizada por responsabilidades.

Camadas principais:

* `models`: representam as entidades do domínio.
* `repositories`: fazem o acesso à base de dados SQLite.
* `services`: concentram regras de negócio e algoritmos.
* `menus`: disponibilizam a interface operacional por consola.
* `database`: cria e liga a base de dados.
* `utils`: contém funções auxiliares, como validações e segurança.

Fluxo funcional:

```text
Menu
↓
Service
↓
Repository
↓
SQLite
```

Principais classes da API interna:

* `MemoryCache`: carrega e mantém dados da BD em memória.
* `TicketService`: atribui tickets automaticamente a técnicos elegíveis.
* `ClienteRepository`: cria, lista, atualiza e remove clientes.
* `TecnicoRepository`: cria, lista, atualiza e remove técnicos.
* `CompetenciaRepository`: cria, lista, atualiza e remove competências.
* `TecnicoCompetenciaRepository`: associa e remove competências dos técnicos.
* `TicketRepository`: cria, lista, atualiza e remove tickets.
* `UtilizadorRepository`: gere utilizadores e autenticação.

Esta organização permite que o menu use métodos bem definidos sem aceder diretamente à base de dados.

## Entrega 5 - Segurança, testes e fiabilidade

Entrega ainda em desenvolvimento.

Já existe:

* Autenticação simples de utilizadores
* Hash de passwords em `src/utils/security.py`
* Controlo básico de opções por perfil no menu
* Testes unitários iniciais do algoritmo da Entrega 3

Previsto:

* Reforço de autorização
* Tratamento de exceções mais completo
* Logs básicos
* Mais testes unitários
* Verificação de vulnerabilidades

## Entrega 6 - Otimização, documentação e defesa

Entrega ainda em desenvolvimento.

Já existe:

* Documentação inicial em `README.md`
* Documentação de requisitos e diagramas em `docs/`
* Proposta do projeto no repositório

Previsto:

* Otimizações finais
* Documentação técnica completa
* Manual de instalação e utilização
* Preparação da apresentação final
