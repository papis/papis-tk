try:
    # py3
    import tkinter as tk
except:
    # py2
    import Tkinter as tk

from papis_tk.app import PapisWidget, Gui
from papis_tk.prompt import Prompt
from papis_tk.list import PapisList

import sys
import logging

import click
from click import echo
import papis.cli
import papis.database


__version__ = '0.1.0'


@click.command()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@papis.cli.query_option()
@click.option(
    '--debug',
    is_flag=True,
    help='enable debug logging'
)
def main(query, debug):
    """A tk based gui for papis"""
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")

    documents = papis.database.get().query(query)
    app = Gui()
    app.main(documents)
