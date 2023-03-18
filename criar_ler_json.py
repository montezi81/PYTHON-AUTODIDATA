import json
# criar ou ler arquivo json
# O ideal é criar um arquivo json a parte e depois colocar dentro das 3 aspas duplas
computador_json = """{
  "marca": "Dell",
  "preco": 15000
}"""

# Lendo uma string json, usando loads
data = json.loads(computador_json)
print(data["preco"])

# Salvar uma string Json
# Crio nome do arquivo computador.json no modo de escrita 'w' = write
# Coloco no modo de formatação utf-8, para caracteres especiais
# O nome de arquivo de saída arquivo_json
# para criar o arquivo coloco o json.dump, coloco o parametro no qual recebeu os dados do json acima e passo a operação que é o arquivo_json

with open ('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)

# Para ler o arquivo criado acima

with open ('computador.json', encoding='utf-8') as arquivo_json:
    string_json = json.load(arquivo_json) # Converte o json para string e guardo em uma variavel
    dicionario_computador_json = json.loads(string_json) # Converte de string para dicionário
    print(dicionario_computador_json["marca"])



