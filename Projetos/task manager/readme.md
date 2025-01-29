# Projeto Gerenciador de Tarefas

### Este projeto é um sistema web desenvolvido com Django que permite gerenciar tarefas com funcionalidades de criação, edição, exclusão e visualização. O sistema também inclui a possibilidade de exportar e importar tarefas de um arquivo CSV.

## Funcionalidades

* Adicionar Tarefas: Insira tarefas com nome, descrição e data de vencimento.
* Editar Tarefas: Atualize informações das tarefas já cadastradas.
* Excluir Tarefas: Remova tarefas que já foram concluídas ou que não são mais necessárias.
* Visualizar Tarefas: Exiba uma lista de todas as tarefas cadastradas.
* Exportar Tarefas para CSV: Salve todas as tarefas em um arquivo CSV para uso externo.
* Importar Tarefas de CSV: Carregue tarefas a partir de um arquivo CSV.

## Instalação

Instale as dependências

```
pip install -r requirements.txt
```
## Configuração

Criando Migração

```
python manage.py makemigrations
```

Aplicando a migração no Banco de Dados

```
python manage.py migrate
```