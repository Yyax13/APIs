from misc import update
update.pip(package="yollor")
update.pip(package="requests")
import requests as r
import json

token = "debf6ffe6409427fea9a0cf27020e78f"

ReqData = r.get(f"http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token={token}")
data = json.loads(ReqData.text)

country = data['country']
text = data['text']
date = data['date']
print(f"No país {country} no dia {date}, as informações sobre o clima são: {text}")