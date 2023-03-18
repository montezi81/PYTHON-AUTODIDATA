import json

desafio = """{
  "name": "John Smith",
  "age": 30,
  "city": "New York",
  "isStudent": true,
  "gpa": 3.5
}"""

with open ('desafio_criando_arquivo_json.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(desafio, arquivo_json)