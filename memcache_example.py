from pymemcache.client.base import Client

ipv4_client_with_port = Client('127.0.0.1:11211')

client = Client('localhost')
client.set('some_key', 'some_value')
result = client.get('some_key')

print(result)