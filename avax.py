import requests
import click
import json


def query(endpoint, method, ip="http://127.0.0.1:9650", **kwargs):
    HEADERS = { 'content-type': 'application/json;', }
    DATA = f'{{ "jsonrpc":"2.0", "id" :1, "method" :"{method}", "params": {json.dumps(kwargs)} }}'
    print(requests.post(**{"url":f"{ip}/{endpoint}", "headers":HEADERS, "data":DATA}).json())

def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

auth_options = [
    click.option('--password', required=True, help='The node password.'),
    click.option('--username', required=True, help='The node username.')
    ]

@click.group()
def guest():
    pass

@click.group()
def auth():
    pass


@guest.command()
def is_bootstrapped():
    query("ext/info", "info.isBootstrapped", chain="X")

@auth.command()
@add_options(auth_options)
def create_user(username, password):
    query("ext/keystore", "keystore.createUser", username=username, password=password)

@auth.command()
@add_options(auth_options)
def create_address(username, password):
    query("ext/bc/X", "avm.createAddress", username=username, password=password)

if __name__ == '__main__':
    cli = click.CommandCollection(sources=[auth, guest])
    cli()
