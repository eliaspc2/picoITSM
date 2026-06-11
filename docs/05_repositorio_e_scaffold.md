# Repositório Git e Estrutura do Projeto

## Repositório

O projeto utiliza Git e encontra-se alojado no GitHub:

- Repositório: `https://github.com/eliaspc2/picoITSM`
- Ramo principal: `main`
- O histórico de commits permite acompanhar a evolução das diferentes entregas.

O convite de acesso ao formador é uma configuração externa ao código e deve ser
confirmado diretamente nas definições de colaboradores do repositório GitHub.

## Estrutura

```text
picoITSM/
├── database/
│   └── picoitsm.db
├── docs/
│   ├── 01_stack_tecnologico.md
│   ├── 02_requisitos.md
│   ├── 03_diagrama_entidade_relacionamento.md
│   ├── 04_diagrama_classes.md
│   └── 05_repositorio_e_scaffold.md
├── src/
│   ├── database/
│   ├── menus/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── tests/
│   ├── utils/
│   └── main.py
├── .gitignore
├── README.md
└── Proposta de Projeto - 10790.pdf
```

## Responsabilidade das Pastas

| Pasta | Conteúdo |
|---|---|
| `database` | Ficheiro da base de dados SQLite. |
| `docs` | Documentação de análise, requisitos e desenho. |
| `src/database` | Ligação, criação e preenchimento inicial da base de dados. |
| `src/menus` | Interface de consola. |
| `src/models` | Entidades do domínio. |
| `src/repositories` | Acesso e operações sobre os dados persistidos. |
| `src/services` | Regras de negócio, cache e algoritmo de atribuição. |
| `src/tests` | Testes automatizados. |
| `src/utils` | Validações e segurança. |
