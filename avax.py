import requests
import click

HEADERS = { 'content-type': 'application/json;', }

@click.group()
def cli():
    pass

@cli.command()
def is_bootstrapped():
    data = '{ "jsonrpc":"2.0", "id" :1, "method" :"info.isBootstrapped", "params": { "chain":"X" } }'
    print(requests.post('http://127.0.0.1:9650/ext/info', headers=HEADERS, data=data).json())

@click.option('--username', required=True, help='The node username.')
@click.option('--password', required=True, help='The node password.')
@cli.command()
def create_user(username, password):
    data = '{ "jsonrpc": "2.0", "id": 1, "method": "keystore.createUser", "params": { "username": "'+username+'", "password": "'+password+'" } }'
    print(requests.post('http://127.0.0.1:9650/ext/keystore', headers=HEADERS, data=data).json())

@click.option('--username', required=True, help='The node username.')
@click.option('--password', required=True, help='The node password.')
@cli.command()
def create_address(username, password):
    data = '{ "jsonrpc":"2.0", "id" :2, "method" :"avm.createAddress", "params" :{ "username":"'+username+'", "password":"'+password+'" } }'
    print(requests.post('http://127.0.0.1:9650/ext/bc/X', headers=HEADERS, data=data).json())

if __name__ == '__main__':
    cli()

