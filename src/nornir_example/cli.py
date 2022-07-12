# System imports
from typing import Optional

# Third party imports
import typer
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

# Private imports
from nornir_example.functions import render_config, write_config, create_dirs

# Settings
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "configs"

# Initialize Typer app
app = typer.Typer(help="Simple Nornir Example")


@app.command()
def init():
    """
    Initialize working directory
    """
    dirs = [OUTPUT_DIR]
    typer.echo("Creating directories...")
    create_dirs(dirs)
    typer.echo("Init complete")


@app.command()
def create_configs(
    template_dir: Optional[str] = typer.Option(
        "", help="Directory to look for configuration templates"
    ),
    output_dir: Optional[str] = typer.Option(
        "", help="Directory to put resulting configs"
    ),
):
    """
    Generate device configurations and put them to local directory.
    """

    nr = InitNornir(config_file="nornir_config.yml")

    # Apply default values if user didn't specify any
    if not template_dir:
        template_dir = TEMPLATE_DIR
    if not output_dir:
        output_dir = OUTPUT_DIR

    print_result(nr.run(task=render_config, template_dir=template_dir))
    print_result(nr.run(task=write_config, output_dir=output_dir))


def main():
    app()


if __name__ == "__main__":
    main()
