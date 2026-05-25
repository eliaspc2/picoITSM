# Diagrama de Classes

## Objetivo

Este diagrama representa a estrutura principal de classes do projeto picoITSM.

O sistema será desenvolvido em Python e terá uma organização simples, adequada a uma aplicação por linha de comandos.

## Classes Principais

As classes principais serão:

- Tecnico
- Cliente
- Competencia
- Ticket
- GestorTickets

## Classe: Tecnico

Representa um técnico responsável pela resolução de tickets.

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| id_tecnico | int | Identificador único do técnico |
| nome | str | Nome do técnico |
| email | str | Email do técnico |
| disponivel | bool | Indica se o técnico está disponível |
| ativo | bool | Indica se o técnico está ativo |
| competencias | list | Lista de competências do técnico |

### Métodos

| Método | Descrição |
|---|---|
| adicionar_competencia() | Adiciona uma competência ao técnico |
| remover_competencia() | Remove uma competência do técnico |
| esta_disponivel() | Verifica se o técnico está disponível |

## Classe: Cliente

Representa um cliente que cria tickets.

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| id_cliente | int | Identificador único do cliente |
| nome | str | Nome do cliente |
| email | str | Email do cliente |
| telefone | str | Contacto telefónico do cliente |

### Métodos

| Método | Descrição |
|---|---|
| atualizar_contacto() | Atualiza os dados de contacto do cliente |

## Classe: Competencia

Representa uma área técnica necessária para resolver tickets.

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| id_competencia | int | Identificador único da competência |
| nome | str | Nome da competência |
| descricao | str | Descrição da competência |

### Métodos

| Método | Descrição |
|---|---|
| atualizar_descricao() | Atualiza a descrição da competência |

## Classe: Ticket

Representa um incidente ou pedido de suporte.

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| id_ticket | int | Identificador único do ticket |
| titulo | str | Título do ticket |
| descricao | str | Descrição do problema |
| prioridade | str | Prioridade do ticket |
| estado | str | Estado atual do ticket |
| cliente | Cliente | Cliente associado ao ticket |
| competencia | Competencia | Competência necessária |
| tecnico | Tecnico | Técnico atribuído |

### Métodos

| Método | Descrição |
|---|---|
| atualizar_estado() | Atualiza o estado do ticket |
| atribuir_tecnico() | Associa um técnico ao ticket |

## Classe: GestorTickets

Classe responsável pela lógica principal de gestão e atribuição de tickets.

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| tickets | list | Lista de tickets |
| tecnicos | list | Lista de técnicos |

### Métodos

| Método | Descrição |
|---|---|
| criar_ticket() | Cria um novo ticket |
| listar_tickets() | Lista os tickets existentes |
| procurar_tecnicos_compativeis() | Procura técnicos com competência adequada |
| calcular_carga_trabalho() | Calcula a carga atual de cada técnico |
| atribuir_ticket_automaticamente() | Atribui o ticket ao técnico mais adequado |

## Relações Entre Classes

- Um Cliente pode ter vários Tickets.
- Um Ticket pertence a um Cliente.
- Um Ticket pode ter uma Competencia necessária.
- Um Tecnico pode ter várias Competencias.
- Um Ticket pode ser atribuído a um Tecnico.
- GestorTickets coordena a criação, consulta e atribuição de Tickets.

## Representação Simplificada

```text
Cliente 1 ─── N Ticket

Tecnico 1 ─── N Ticket

Tecnico N ─── N Competencia

Ticket 1 ─── 1 Competencia

GestorTickets ─── gere ─── Ticket
GestorTickets ─── consulta ─── Tecnico