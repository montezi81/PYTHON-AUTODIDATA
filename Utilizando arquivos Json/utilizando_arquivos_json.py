# JSON (Javascript Object Notation)

import json

with open ('usuario1.json',encoding='utf-8') as arquivo_json:
   data = json.load(arquivo_json) # Convertendo o arquivo json em uma string
   print(data["nome"])
