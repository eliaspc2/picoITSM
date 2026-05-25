# Diagrama Entidade-Relacionamento

## Entidades Principais

O projeto picoITSM terá uma base de dados simples, adequada a uma aplicação por linha de comandos.

As entidades principais serão:

- Técnicos
- Clientes
- Competências
- Tickets
- Técnico_Competência

## Entidade: tecnicos

Representa os técnicos responsáveis pelo tratamento dos tickets.

| Campo | Tipo | Descrição |
|---|---|---|
| id_tecnico | INTEGER | Identificador único do técnico |
| nome | TEXT | Nome do técnico |
| email | TEXT | Email do técnico |
| disponivel | INTEGER | Indica se o técnico está disponível |
| ativo | INTEGER | Indica se o técnico está ativo no sistema |

## Entidade: clientes

Representa os clientes que reportam incidentes ou pedidos de suporte.

| Campo | Tipo | Descrição |
|---|---|---|
| id_cliente | INTEGER | Identificador único do cliente |
| nome | TEXT | Nome do cliente |
| email | TEXT | Email do cliente |
| telefone | TEXT | Contacto telefónico do cliente |

## Entidade: competencias

Representa as áreas técnicas necessárias para resolver tickets.

| Campo | Tipo | Descrição |
|---|---|---|
| id_competencia | INTEGER | Identificador único da competência |
| nome | TEXT | Nome da competência |
| descricao | TEXT | Descrição da competência |

## Entidade: tecnico_competencia

Tabela intermédia que associa técnicos às suas competências.

| Campo | Tipo | Descrição |
|---|---|---|
| id_tecnico | INTEGER | Identificador do técnico |
| id_competencia | INTEGER | Identificador da competência |

## Entidade: tickets

Representa os pedidos de suporte ou incidentes registados no sistema.

| Campo | Tipo | Descrição |
|---|---|---|
| id_ticket | INTEGER | Identificador único do ticket |
| titulo | TEXT | Título do ticket |
| descricao | TEXT | Descrição do problema |
| prioridade | TEXT | Prioridade do ticket |
| estado | TEXT | Estado atual do ticket |
| id_cliente | INTEGER | Cliente associado ao ticket |
| id_competencia | INTEGER | Competência necessária para resolver o ticket |
| id_tecnico | INTEGER | Técnico atribuído ao ticket |

## Relações

- Um cliente pode criar vários tickets.
- Um ticket pertence a um único cliente.
- Um ticket pode ter uma competência associada.
- Uma competência pode estar associada a vários tickets.
- Um técnico pode ter várias competências.
- Uma competência pode pertencer a vários técnicos.
- Um técnico pode ter vários tickets atribuídos.
- Um ticket pode ter um técnico atribuído.

## Representação Simplificada

```text
clientes 1 ─── N tickets

tecnicos 1 ─── N tickets

competencias 1 ─── N tickets

tecnicos N ─── N competencias
        através de tecnico_competencia