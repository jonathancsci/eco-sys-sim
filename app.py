import typer
from eco_sys_sim.environment import Environment

environment = Environment(rows=5, cols=10)


def main(
    name: str = typer.Option(prompt="Please enter your name", help="Your legal name"),
):
    print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(main)
