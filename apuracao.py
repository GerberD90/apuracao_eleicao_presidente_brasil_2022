import requests

try:
    URL = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
    resultado = requests.get(URL).json()
    print('_-'*28)
    print(f"| {'Nome do Canditado':<20} | {'Nº':^2} | {'Votos':^10} | {'% Votos':^10}  |")
    for candidato in resultado['cand']:
        print(f"| {candidato['nm']: <20} | {candidato['n']:^2} | {candidato['vap']:^10} | {candidato['pvap']:^9}{'%':<1}  |")
    print('_-'*28)
    print(f"\nUrnas Apuradas: {resultado['pst']}%")
except:
    print('!ERROR!')
