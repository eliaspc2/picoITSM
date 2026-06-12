# Análise de Vulnerabilidades

## Objetivo

Este documento identifica os principais riscos de segurança do picoITSM e as
medidas aplicadas na Entrega 5.

## Vulnerabilidades Identificadas e Tratamento

| Risco | Impacto | Medida aplicada | Estado |
|---|---|---|---|
| Passwords guardadas com hash simples SHA-256 | Um atacante com acesso à base de dados poderia testar passwords com facilidade. | Implementado hash PBKDF2 com salt e várias iterações. | Mitigado |
| Utilizadores antigos com hash SHA-256 | Mudança de algoritmo poderia impedir login de utilizadores existentes. | A verificação de password aceita PBKDF2 e SHA-256 antigo. | Mitigado |
| Técnico conseguir consultar tickets de outros técnicos | Exposição indevida de informação operacional. | Utilizadores técnicos têm `id_tecnico` e só veem tickets atribuídos a esse técnico. | Mitigado |
| Administrador e técnico com o mesmo menu funcional | Risco de acesso a operações administrativas por chamada direta. | Métodos administrativos validam explicitamente o perfil com `exigir_admin()`. | Mitigado |
| Alterações sem rastreabilidade | Dificuldade em perceber quem alterou dados. | Logs em texto com data/hora, utilizador, ação, entidade e detalhes. | Mitigado |
| Integridade referencial SQLite desligada em novas ligações | Possibilidade de criar relações inválidas entre tabelas. | `PRAGMA foreign_keys = ON` ativado em cada ligação. | Mitigado |
| Entradas inválidas do utilizador | Erros ou dados inconsistentes. | Validações para campos obrigatórios, emails, IDs, booleanos, prioridades e estados. | Mitigado |
| Falta de cobertura de testes | Regressões não detetadas. | Adicionados testes de algoritmo, autorização, segurança, logger e validações. | Mitigado parcialmente |

## Riscos Residuais

- A aplicação continua a ser uma CLI académica, sem gestão avançada de sessões.
- Não existe rotação automática de logs.
- Não existe bloqueio de conta após várias tentativas falhadas de login.
- A base de dados SQLite continua a ser um ficheiro local, pelo que a proteção
  do ficheiro depende das permissões do sistema operativo.

## Conclusão

A Entrega 5 melhora a confidencialidade, integridade e rastreabilidade do
sistema, cobrindo os requisitos principais de autenticação, autorização, logs,
testes e análise de vulnerabilidades.
