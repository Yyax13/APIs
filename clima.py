import requests as r
import json

# Defina sua variável de token com o valor correto
token = "debf6ffe6409427fea9a0cf27020e78f"

ReqData = r.get(f"http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token={token}")
data = json.loads(ReqData.text)

country = data[0]['country']
text = data[0]['text']
date = data[0]['date']
print(f"No país {country} no dia {date}, as informações sobre o clima são: {text}")
