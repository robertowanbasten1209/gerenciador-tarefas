# Gerenciador de Tarefas

Programa de terminal para organizar tarefas, com um menu interativo onde é possível adicionar, listar, concluir e excluir tarefas. Os dados ficam guardados em um banco de dados local.

## Funcionalidades

- Adicionar uma nova tarefa
- Listar as tarefas, mostrando se estão pendentes ou concluídas
- Marcar uma tarefa como concluída
- Excluir uma tarefa

## Tecnologias

- Python
- SQLite (módulo `sqlite3`, que já vem com o Python)

## Como rodar

1. Instale o [Python](https://www.python.org/downloads/).
2. Baixe o projeto:
   ```
   git clone https://github.com/seu-usuario/gerenciador-tarefas.git
   ```
3. Entre na pasta do projeto:
   ```
   cd gerenciador-tarefas
   ```
4. Execute o programa:
   ```
   python main.py
   ```

O arquivo do banco (`tarefas.db`) é criado automaticamente na primeira execução.

## Próximos passos

- Tratar erros de digitação no menu
- Separar o código em mais de um arquivo
- Criar uma versão web com Flask