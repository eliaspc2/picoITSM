# Diagrama de Classes

## Lógica de Domínio e Arquitetura

O diagrama representa as classes existentes na versão atual. Ao contrário da
versão inicial deste documento, não inclui métodos ou classes que não estejam
presentes no código.

```mermaid
classDiagram
    class Utilizador {
        +username: str
        +password: str
        +perfil: str
        +ativo: int
        +id_tecnico: int
    }

    class Tecnico {
        +nome: str
        +email: str
        +disponivel: int
        +ativo: int
    }

    class Cliente {
        +nome: str
        +email: str
        +telefone: str
    }

    class Competencia {
        +nome: str
        +descricao: str
    }

    class Ticket {
        +titulo: str
        +descricao: str
        +prioridade: str
        +estado: str
        +id_cliente: int
        +id_competencia: int
        +id_tecnico: int
    }

    class Menu {
        +mostrar_menu()
        +menu_clientes()
        +menu_tecnicos()
        +menu_competencias()
        +menu_tickets()
        +menu_utilizadores()
    }

    class TicketService {
        +tecnico_tem_competencia(id_tecnico, id_competencia)
        +calcular_carga_tecnico(id_tecnico)
        +escolher_tecnico(id_competencia)
        +criar_ticket_com_atribuicao(...)
    }

    class MemoryCache {
        +carregar()
        +recarregar()
        +obter_dados()
        +obter(chave)
    }

    class DatabaseConnection {
        +ligar_bd()
        +fechar_bd(conn)
    }

    class UtilizadorRepository
    class TecnicoRepository
    class ClienteRepository
    class CompetenciaRepository
    class TecnicoCompetenciaRepository
    class TicketRepository

    Menu --> TicketService : cria tickets
    Menu --> MemoryCache : atualiza dados
    Menu --> UtilizadorRepository
    Menu --> TecnicoRepository
    Menu --> ClienteRepository
    Menu --> CompetenciaRepository
    Menu --> TecnicoCompetenciaRepository
    Menu --> TicketRepository
    TicketService --> Ticket : instancia
    TicketService --> TicketRepository : persiste
    TicketService --> MemoryCache : sincroniza
    MemoryCache --> UtilizadorRepository
    MemoryCache --> TecnicoRepository
    MemoryCache --> ClienteRepository
    MemoryCache --> CompetenciaRepository
    MemoryCache --> TicketRepository
    UtilizadorRepository --> DatabaseConnection
    TecnicoRepository --> DatabaseConnection
    ClienteRepository --> DatabaseConnection
    CompetenciaRepository --> DatabaseConnection
    TecnicoCompetenciaRepository --> DatabaseConnection
    TicketRepository --> DatabaseConnection
```

## Entidades Previstas no Âmbito Completo

As classes seguintes resultam dos requisitos do enunciado e deverão ser
adicionadas quando o inventário e a disponibilidade horária forem implementados:

```mermaid
classDiagram
    class Ativo {
        +nome: str
        +tipo: str
        +fabricante: str
        +modelo: str
        +numero_serie: str
        +estado: str
        +id_cliente: int
    }

    class Disponibilidade {
        +id_tecnico: int
        +dia_semana: int
        +hora_inicio: time
        +hora_fim: time
    }

    class Ticket
    class Cliente
    class Tecnico

    Cliente "1" --> "0..*" Ativo : possui
    Ticket "0..*" --> "0..*" Ativo : afeta
    Tecnico "1" --> "0..*" Disponibilidade : define
```

## Responsabilidades

- As entidades transportam os dados do domínio.
- O `Menu` gere a interação e valida os dados introduzidos.
- O `TicketService` contém o algoritmo de atribuição automática.
- A `MemoryCache` mantém em memória os dados carregados da base de dados.
- Os repositórios isolam as operações SQL.
- A `DatabaseConnection` centraliza a abertura e o fecho das ligações SQLite.
