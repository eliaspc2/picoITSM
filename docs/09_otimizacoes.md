# Otimizações Aplicadas

## Objetivo

Este documento resume as principais otimizações técnicas aplicadas no picoITSM
e a razão da sua utilização.

## Heap / Priority Queue

O algoritmo de atribuição automática utiliza `heapq`, a implementação de heap
da biblioteca padrão do Python.

Justificação:

- permite ordenar candidatos pela carga de trabalho;
- evita percorrer manualmente várias vezes a lista de técnicos;
- torna clara a regra de escolha do técnico com menor carga;
- em caso de empate, o `id_tecnico` garante uma escolha determinística.

Critérios usados:

1. competência necessária;
2. técnico ativo;
3. disponibilidade como prioridade;
4. menor carga de tickets não fechados.

Se nenhum técnico disponível cumprir a competência, o sistema escolhe um
técnico ativo com essa competência e menor carga.

## Cache em Memória

A classe `MemoryCache` carrega dados da base de dados para memória.

Justificação:

- reduz consultas repetidas à base de dados;
- centraliza os dados usados pelos menus e serviços;
- facilita o algoritmo de atribuição, que trabalha sobre listas em memória;
- permite recarregar os dados após alterações.

## Separação por Camadas

O projeto está dividido em:

- modelos;
- menus;
- serviços;
- repositórios;
- base de dados;
- utilitários;
- testes.

Justificação:

- melhora a organização;
- facilita manutenção;
- separa interface, regras de negócio e persistência;
- torna o projeto mais fácil de explicar na defesa.

## Logs Centralizados

O `Logger` centraliza o registo de alterações em ficheiro de texto.

Justificação:

- evita repetir lógica de escrita em ficheiros;
- garante formato consistente;
- inclui o utilizador autenticado;
- ajuda na auditoria das ações realizadas.

## Segurança de Passwords

As passwords são guardadas com PBKDF2 e salt.

Justificação:

- é mais seguro do que SHA-256 simples;
- dificulta ataques por força bruta;
- mantém compatibilidade com hashes antigos para não bloquear utilizadores já
  existentes.

## Chaves Estrangeiras SQLite

Cada ligação ativa `PRAGMA foreign_keys = ON`.

Justificação:

- reforça integridade referencial;
- evita relações inválidas entre tickets, técnicos, clientes e competências.

## Testes Automatizados

Foram adicionados testes unitários com `unittest`.

Justificação:

- validam o algoritmo principal;
- verificam autorização por perfil;
- confirmam funcionamento de segurança, logger e validações;
- reduzem risco de regressões antes da defesa.

## Conclusão

As otimizações aplicadas tornam o projeto mais robusto, organizado e adequado
ao contexto académico, mantendo a simplicidade necessária para uma aplicação
CLI.
