import matplotlib.pyplot as plt
import typer
from eco_sys_sim.ecosystem import Ecosystem
from eco_sys_sim.status import Status, MaxIterReached, UserTerminated
from rich.console import Console
from rich.table import Table


console = Console()


def main(
    rows: int = typer.Option(
        default=5, prompt="Rows", help="Number of rows in the grid map"
    ),
    cols: int = typer.Option(
        default=10, prompt="Columns", help="Number of columns in the grid map"
    ),
    probability_of_obstacles: float = typer.Option(
        default=0.2,
        prompt="Probability of obstacles",
        help="Probability that a grid will be an obstacle (%)",
    ),
    num_iters: int = typer.Option(
        default=100,
        prompt="Number of iterations (at 10Hz)",
        help="Number of iterations to run the simulation for. The simulation runs at a rate of 10 Hz",
    ),
    init_num_bears: int = typer.Option(
        default=5, prompt="Initial number of bears", help="Initial number of bears"
    ),
    init_num_wolves: int = typer.Option(
        default=15, prompt="Initial number of wolves", help="Initial number of wolves"
    ),
    init_num_foxes: int = typer.Option(
        default=25, prompt="Initial number of foxes", help="Initial number of foxes"
    ),
    init_num_deer: int = typer.Option(
        default=25, prompt="Initial number of deer", help="Initial number of deer"
    ),
    init_num_rabbits: int = typer.Option(
        default=60, prompt="Initial number of rabbits", help="Initial number of rabbits"
    ),
):
    if not (0 <= probability_of_obstacles < 1):
        console.print(
            f":x: Error: probability_of_obstacles must be in the range [0, 1), got {probability_of_obstacles}",
            style="bold",
        )
        raise typer.Exit(code=1)

    init_table = create_init_table(
        rows,
        cols,
        probability_of_obstacles,
        num_iters,
        init_num_bears,
        init_num_wolves,
        init_num_foxes,
        init_num_deer,
        init_num_rabbits,
    )
    console.print(
        "\nStarting simulation with the following initial conditions:", style="bold"
    )
    console.print(init_table)

    try:
        ecosystem = Ecosystem(
            rows,
            cols,
            probability_of_obstacles,
            init_num_bears,
            init_num_wolves,
            init_num_foxes,
            init_num_deer,
            init_num_rabbits,
        )
        returned_status, final_populations = ecosystem.run_simulation(num_iters)
        final_table = create_final_table(final_populations)

        match returned_status:
            case MaxIterReached():
                console.print(f"{num_iters} iterations completed\n")
            case UserTerminated():
                console.print(":stop_sign: Plot window closed\n")

        console.print("Exiting simulation with the following end state:", style="bold")
        console.print(final_table)

    except Exception as e:
        # console.print("Oh no, something went wrong")
        # console.print(e)
        # raise typer.Exit(code=1)
        raise Exception(e)


def create_init_table(
    rows,
    cols,
    probability_of_obstacles,
    num_iters,
    init_num_bears,
    init_num_wolves,
    init_num_foxes,
    init_num_deer,
    init_num_rabbits,
) -> Table:
    init_table = Table("Variable", "Value")
    init_table.add_row(":up-down_arrow:  Rows", f"{rows}")
    init_table.add_row(":left_right_arrow:  Columns", f"{cols}")
    init_table.add_row(":game_die: Chance of obstacles", f"{probability_of_obstacles}")
    init_table.add_row(":timer_clock:  Iterations", f"{num_iters}")
    init_table.add_row(":bear: Bears", f"{init_num_bears}")
    init_table.add_row(":wolf: Wolves", f"{init_num_wolves}")
    init_table.add_row(":fox_face: Foxes", f"{init_num_foxes}")
    init_table.add_row(":deer: Deer", f"{init_num_deer}")
    init_table.add_row(":rabbit: Rabbits", f"{init_num_rabbits}")
    return init_table


def create_final_table(final_populations: dict[str, int]) -> Table:
    final_table = Table("Animal", "Population")
    final_table.add_row(":bear: Bears", f"{final_populations['bear']}")
    final_table.add_row(":wolf: Wolves", f"{final_populations['wolf']}")
    final_table.add_row(":fox_face: Foxes", f"{final_populations['fox']}")
    final_table.add_row(":deer: Deer", f"{final_populations['deer']}")
    final_table.add_row(":rabbit: Rabbits", f"{final_populations['rabbit']}")
    return final_table


if __name__ == "__main__":
    typer.run(main)
