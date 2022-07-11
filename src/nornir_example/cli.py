#!/usr/bin/env python3
from typing import Optional

import typer
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

from nornir_example.functions import render_config, write_config

app = typer.Typer(help="Exactpro Network Configuration Manager")


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
        template_dir = "templates"
    if not output_dir:
        output_dir = "configs"

    print_result(nr.run(task=render_config, template_dir=template_dir))
    print_result(nr.run(task=write_config, output_dir=output_dir))


def main():
    app()


if __name__ == "__main__":
    main()
