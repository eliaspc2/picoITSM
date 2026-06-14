# Manual de Instalação e Utilização

## Requisitos

- Python 3 instalado.
- Terminal ou linha de comandos.
- Git, caso seja necessário clonar o repositório.

O projeto não necessita de bibliotecas externas.

## Instalação

1. Abrir a pasta do projeto:

```bash
cd picoITSM
```

2. Criar ou atualizar as tabelas da base de dados:

```bash
python src/database/init_db.py
```

3. Inserir dados de teste:

```bash
python src/database/seed_db.py
```

4. Iniciar a aplicação:

```bash
python src/main.py
```

## Utilizadores de Teste

| Username | Password | Perfil | Associação |
|---|---|---|---|
| `admin` | `admin123` | `ADMIN` | Sem técnico associado |
| `user` | `user123` | `TECNICO` | João Silva |
| `maria` | `tecnico123` | `TECNICO` | Maria Santos |

## Como Usar

### Login

Ao iniciar a aplicação, o sistema pede username e password. Depois do login,
apresenta o menu principal de acordo com o perfil autenticado.

### Perfil ADMIN

O administrador consegue:

- gerir clientes;
- gerir tickets;
- gerir técnicos;
- gerir competências;
- gerir utilizadores;
- ver todos os tickets;
- associar competências a técnicos.

### Perfil TECNICO

O técnico consegue:

- consultar tickets;
- alterar/fechar tickets permitidos pelo seu perfil;
- ver apenas tickets atribuídos ao técnico associado ao seu login.

## Fluxo Principal de Demonstração

1. Entrar com `admin`.
2. Listar técnicos e competências.
3. Criar um ticket com uma competência existente.
4. Confirmar que o sistema atribui automaticamente o ticket.
5. Entrar com `user`.
6. Confirmar que o técnico vê apenas os seus tickets.
7. Entrar com `maria`.
8. Confirmar que a técnica vê apenas os tickets dela.

## Testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s src/tests -v
```

Os testes cobrem:

- algoritmo de atribuição automática;
- autorização de tickets por perfil;
- validações;
- segurança de passwords;
- registo de logs.

## Logs

As alterações de dados são registadas em:

```text
logs/picoitsm.log
```

Cada linha contém:

```text
data/hora | utilizador | ação | entidade | detalhes
```

## Limitações Assumidas

As funcionalidades de inventário de ativos de hardware/software e
disponibilidade horária detalhada foram modeladas na análise, mas não foram
implementadas nesta versão final. A versão entregue foca-se na gestão de
clientes, técnicos, competências, utilizadores, tickets, atribuição automática,
segurança, logs e testes.
