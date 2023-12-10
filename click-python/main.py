import click

@click.group
def cli():
    pass

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    click.echo(f"Hello {name}!")

PRIORITIES = {
    'o': 'Optional',
    'l': 'Low',
    'm': 'Medium',
    'h': 'High',
    'c': 'Critical'
}

@click.command()
@click.argument('priority', type=click.Choice(PRIORITIES.keys()), default='m')
@click.argument('todofile', type=click.Path(exists=False), required=0)
@click.option('-n', '--name', prompt='Enter todo name', help='Name of the todo')
@click.option('-d', '--description', prompt='Enter todo description', help='Description of the todo')
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else 'todo.txt'
    with open(filename, 'a+') as f:
        f.write(f'{PRIORITIES[priority]}: {name} - {description}\n')

@click.command()
@click.argument('idx', type=int, required=1)
def delete_todo(idx):
    with open('todo.txt', 'r') as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open('todo.txt', 'w') as f:
        f.write('\n'.join(todo_list))
        f.write('\n')

@click.command()
@click.option('-p', '--priority', type=click.Choice(PRIORITIES.keys()), default=None)
@click.argument('todofile', type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else 'todo.txt'
    with open(filename, 'r') as f:
        todo_list = f.read().splitlines()
        if priority is not None:
            todo_list = [todo for todo in todo_list if todo.startswith(PRIORITIES[priority])]
        for idx, todo in enumerate(todo_list):
            click.echo(f'{idx}: {todo}')

cli.add_command(hello)
cli.add_command(add_todo)
cli.add_command(delete_todo)
cli.add_command(list_todos)

if __name__ == '__main__':
    cli()