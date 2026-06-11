# Requisitos Funcionais e Não-Funcionais

## Âmbito

O picoITSM permite gerir os intervenientes e recursos de suporte informático,
registar incidentes ou pedidos e atribuí-los automaticamente ao técnico mais
adequado. O inventário de ativos e a disponibilidade horária fazem parte do
âmbito funcional completo definido pelo enunciado, embora ainda não estejam
implementados na versão atual.

## Atores

- **Administrador:** gere utilizadores, técnicos, competências, clientes,
  ativos e tickets.
- **Técnico:** consulta e trata informação operacional permitida pelo seu
  perfil.

## Requisitos Funcionais

| ID | Requisito | Prioridade | Estado atual |
|---|---|---|---|
| RF01 | Autenticar utilizadores ativos através de username e password. | Alta | Implementado |
| RF02 | Apresentar opções de menu de acordo com o perfil autenticado. | Alta | Implementado |
| RF03 | Criar, consultar, editar e remover clientes. | Alta | Implementado |
| RF04 | Criar, consultar, editar e remover técnicos. | Alta | Implementado |
| RF05 | Definir se um técnico está ativo e disponível. | Alta | Implementado |
| RF06 | Criar, consultar, editar e remover competências. | Alta | Implementado |
| RF07 | Associar e remover competências de técnicos. | Alta | Implementado |
| RF08 | Criar, consultar, editar e remover tickets. | Alta | Implementado |
| RF09 | Associar cada ticket a um cliente e a uma competência necessária. | Alta | Implementado |
| RF10 | Definir prioridade e atualizar o estado de um ticket. | Alta | Implementado |
| RF11 | Atribuir automaticamente um ticket a um técnico elegível. | Alta | Implementado |
| RF12 | Considerar competência, disponibilidade e carga de trabalho na atribuição. | Alta | Implementado |
| RF13 | Permitir que um ticket fique sem técnico quando não existam candidatos. | Média | Implementado |
| RF14 | Criar, consultar, editar, ativar e remover utilizadores. | Alta | Implementado |
| RF15 | Guardar os dados em SQLite e carregá-los ao iniciar a aplicação. | Alta | Implementado |
| RF16 | Registar ativos de hardware e software. | Alta | Por implementar |
| RF17 | Consultar, editar e remover ativos registados. | Alta | Por implementar |
| RF18 | Associar um ativo a um cliente e, quando aplicável, a um ticket. | Média | Por implementar |
| RF19 | Registar períodos de disponibilidade horária dos técnicos. | Média | Por implementar |
| RF20 | Considerar a disponibilidade horária na atribuição automática. | Média | Por implementar |

## Regras de Negócio

| ID | Regra |
|---|---|
| RN01 | Apenas técnicos ativos e disponíveis podem receber tickets automaticamente. |
| RN02 | O técnico tem de possuir a competência exigida pelo ticket. |
| RN03 | A carga corresponde ao número de tickets atribuídos que não estejam fechados. |
| RN04 | Entre técnicos elegíveis, é escolhido o que tiver menor carga. |
| RN05 | Um ticket fechado deixa de contar para a carga do técnico. |
| RN06 | Clientes, técnicos e competências com relações existentes não devem ser removidos sem tratamento dessas relações. |
| RN07 | Apenas administradores podem gerir técnicos, competências e utilizadores. |
| RN08 | Cada username, email de cliente, email de técnico e nome de competência deve ser único. |

## Requisitos Não-Funcionais

| ID | Categoria | Requisito |
|---|---|---|
| RNF01 | Usabilidade | A interface deve apresentar menus e mensagens claras em português. |
| RNF02 | Validação | Campos obrigatórios, emails, IDs, prioridades e estados devem ser validados. |
| RNF03 | Persistência | Os dados devem permanecer disponíveis após o encerramento da aplicação. |
| RNF04 | Organização | O código deve estar separado em modelos, menus, serviços, repositórios, base de dados e utilitários. |
| RNF05 | Manutenção | As responsabilidades das classes e funções devem ser claras e permitir evolução futura. |
| RNF06 | Segurança | As passwords não devem ser guardadas em texto simples e o acesso deve respeitar perfis. |
| RNF07 | Fiabilidade | Erros de utilização não devem provocar o encerramento inesperado da aplicação. |
| RNF08 | Testabilidade | As regras principais devem possuir testes automatizados. |
| RNF09 | Desempenho | A escolha de técnico deve usar uma fila de prioridade para ordenar candidatos. |
| RNF10 | Compatibilidade | A aplicação deve funcionar com Python 3 em Windows e sistemas Unix. |
| RNF11 | Rastreabilidade | O desenvolvimento deve ser registado num repositório Git alojado no GitHub. |

## Critérios de Aceitação Principais

1. Um utilizador válido consegue autenticar-se e abrir o menu correspondente ao perfil.
2. Um administrador consegue gerir clientes, técnicos, competências, utilizadores e tickets.
3. Ao criar um ticket, o sistema escolhe o técnico disponível com a competência exigida e menor carga.
4. Quando não existe técnico elegível, o ticket é guardado sem atribuição.
5. Os dados mantêm-se após fechar e voltar a iniciar a aplicação.
6. Os testes automatizados do algoritmo terminam com sucesso.
