# Requisitos Funcionais e Não-Funcionais

## Requisitos Funcionais

O desenvolvimento do sistema seguirá uma ordem progressiva de implementação das funcionalidades.

### Menu Principal
- Apresentar menu principal da aplicação
- Permitir navegação entre módulos
- Permitir encerramento da aplicação

### Gestão de Técnicos
- Criar técnicos
- Editar técnicos
- Remover técnicos
- Consultar lista de técnicos
- Definir disponibilidade do técnico

### Gestão de Clientes
- Criar clientes
- Editar clientes
- Remover clientes
- Consultar lista de clientes

### Gestão de Competências
- Criar competências
- Associar competências a técnicos
- Consultar competências existentes

### Gestão de Tickets
- Criar tickets
- Associar ticket a cliente
- Definir prioridade do ticket
- Definir competência necessária
- Atualizar estado do ticket
- Consultar tickets existentes

### Atribuição Automática de Tickets
- Selecionar automaticamente o técnico mais adequado
- Verificar competências do técnico
- Verificar carga de trabalho atual
- Verificar disponibilidade do técnico

### Persistência de Dados
- Guardar dados em SQLite
- Carregar dados da base de dados

## Requisitos Não-Funcionais

### Simplicidade
O sistema deverá ser simples e adequado ao contexto académico do projeto.

### Organização do Código
O projeto deverá possuir uma estrutura modular e organizada.

### Manutenção
O código deverá permitir futuras alterações e expansão de funcionalidades.

### Persistência
Os dados deverão permanecer guardados após encerramento da aplicação.

### Fiabilidade
O sistema deverá validar dados introduzidos pelo utilizador e evitar erros críticos durante a execução.

### Compatibilidade
O sistema deverá funcionar em ambiente Windows com Python instalado.

### Controlo de Versões
O projeto deverá utilizar Git e GitHub para registo das alterações realizadas.