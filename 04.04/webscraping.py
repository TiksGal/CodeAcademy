import requests

r = requests.get('http://python.org/blabla')
if r.ok:
    print('važiuojam toliau!')
else:
    print(f'Klaida! kodas {r.status_code}')
# Klaida! kodas 404