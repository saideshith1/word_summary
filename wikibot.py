from mylib.bot import search
import click

@click.command()
@click.option('--name', prompt='webpage to search', help='webpage we want to search')
@click.option('--sentences', prompt='number sentences', help='number of sentences u want to print')
def search_cli(name = "Microsoft", sentences = 1):
    result = search(name, sentences=sentences)
    click.echo(result)

if __name__ == '__main__':
    search_cli()