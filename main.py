import typer
from trogon import Trogon
from typer.main import get_group


app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def tui(context: typer.Context):
    Trogon(get_group(app), click_context=context).run()


if __name__ == "__main__":
    app()
