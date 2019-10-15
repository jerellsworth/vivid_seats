#!/usr/bin/env python

import os
import shutil

import click
import requests
import yaml

REPO_PATH = os.path.dirname(os.path.realpath(__file__))
CONF_PATH = os.path.join(REPO_PATH, 'conf.yml')
MIG_PATH = os.path.join(REPO_PATH, 'migs')

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

    click.echo('# get tickets for event 1')
    resp = requests.get('{}/events/1/tickets'.format(host))
    click.echo(resp.text)
    click.echo('# get tickets for event 2')
    resp = requests.get('{}/events/2/tickets'.format(host))
    click.echo(resp.text)

    click.echo('# posting new ticket')
    data = dict(event_id=1, seller_id=1, section='CHEAP', seat_row=99, qty=12,
                price_each=0.01)
    resp = requests.post('{}/tickets'.format(host), json=data)
    resp = requests.get('{}/events/1/tickets'.format(host))
    click.echo(resp.text)

    click.echo('# selling a ticket')
    data = dict(customer_id=1, qty=1)
    resp = requests.put('{}/tickets/1/purchase'.format(host), json=data)

    click.echo('# get best ticket for event 1')
    resp = requests.get('{}/events/1/tickets/best'.format(host))
    click.echo(resp.text)

if __name__ == '__main__':
    cli()
