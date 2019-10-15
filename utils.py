#!/usr/bin/env python

import os
import shutil

import click
import requests
import yaml

REPO_PATH = os.path.dirname(os.path.realpath(__file__))
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

@cli.command()
def webserver():
    from api.api import app
    app.run()

@cli.command()
def tests():
    # TODO build a proper test with unittests
    host = 'http://localhost:5000'

    click.echo('get tickets for event 1')
    resp = requests.get('{}/events/1/tickets'.format(host))
    click.echo(resp.text)
    click.echo('get tickets for event 2')
    resp = requests.get('{}/events/2/tickets'.format(host))
    click.echo(resp.text)

    click.echo('get best ticket for event 1')
    resp = requests.get('{}/events/1/tickets/best'.format(host))
    click.echo(resp.text)

if __name__ == '__main__':
    cli()
