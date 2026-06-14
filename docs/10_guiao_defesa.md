# Guião de Defesa

## Objetivo da Demonstração

Demonstrar que o picoITSM permite gerir tickets de suporte, técnicos,
competências, clientes e utilizadores, aplicando atribuição automática,
persistência, autenticação, autorização, logs e testes.

## Ordem Recomendada

### 1. Apresentar o Projeto

Explicar que o picoITSM é uma aplicação CLI inspirada em sistemas ITSM, focada
em:

- gestão de tickets;
- gestão de técnicos;
- gestão de competências;
- atribuição automática;
- segurança;
- persistência em SQLite.

### 2. Mostrar a Estrutura

Mostrar rapidamente as pastas:

- `src/models`;
- `src/repositories`;
- `src/services`;
- `src/menus`;
- `src/database`;
- `src/utils`;
- `src/tests`;
- `docs`.

Explicar a arquitetura:

```text
Menu -> Service -> Repository -> SQLite
```

### 3. Demonstrar Login ADMIN

Entrar com:

```text
admin / admin123
```

Mostrar que o administrador tem acesso a:

- clientes;
- tickets;
- técnicos;
- competências;
- utilizadores.

### 4. Demonstrar Atribuição Automática

Criar um ticket novo e escolher uma competência.

Explicar que o sistema:

1. procura técnicos ativos com a competência;
2. dá prioridade a técnicos disponíveis;
3. calcula a carga de tickets não fechados;
4. usa uma heap para escolher o menor;
5. atribui o ticket automaticamente.

Se nenhum técnico disponível existir, o sistema atribui ao técnico ativo com a
competência e menor carga.

### 5. Demonstrar Login TECNICO

Entrar com:

```text
user / user123
```

Mostrar que este utilizador está associado ao João Silva e vê apenas os seus
tickets.

Depois, se necessário, entrar com:

```text
maria / tecnico123
```

Mostrar que Maria vê apenas os tickets atribuídos a ela.

### 6. Demonstrar Logs

Abrir:

```text
logs/picoitsm.log
```

Explicar o formato:

```text
data/hora | utilizador | ação | entidade | detalhes
```

### 7. Demonstrar Testes

Executar:

```bash
python -m unittest discover -s src/tests -v
```

Explicar que os testes cobrem:

- algoritmo de atribuição;
- autorização por perfil;
- logger;
- passwords;
- validações.

### 8. Explicar Segurança

Pontos principais:

- autenticação;
- perfis `ADMIN` e `TECNICO`;
- técnico vê apenas os seus tickets;
- password com PBKDF2;
- logs com utilizador autenticado;
- análise de vulnerabilidades em `docs/07_analise_vulnerabilidades.md`.

### 9. Limitações Assumidas

Explicar claramente:

- ativos de hardware/software foram modelados, mas não implementados;
- disponibilidade horária detalhada foi modelada, mas não implementada;
- a disponibilidade usada atualmente é o campo simples disponível/indisponível.

Estas limitações estão documentadas e ficam como trabalho futuro.

## Frase de Fecho

O projeto cumpre o objetivo principal: implementar uma aplicação ITSM funcional
com persistência, camadas organizadas, algoritmo de atribuição automática,
segurança, logs, testes e documentação técnica.
