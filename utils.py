#!/usr/bin/env python

import os
import shutil

import click
import yaml

REPO_PATH = os.path.dirname(os.path.realpath(__file__))
MIG_PATH = os.path.join(REPO_PATH, 'migs')
CONF_PATH = os.path.join(REPO_PATH, 'conf.yml')

@click.group()
def cli():
    pass

@cli.command()
def init():
    db_path = os.path.join(REPO_PATH, 'tickets.db')
    shutil.copyfile(os.path.join(MIG_PATH, 'sample.db'), db_path)
    with open(CONF_PATH, 'w') as f_conf:
        yaml.dump(dict(db_path=db_path), f_conf)
    click.echo('initialized')

if __name__ == '__main__':
    cli()
