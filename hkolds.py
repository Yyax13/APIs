from misc import update
update.pip(package="yollor")
update.pip(package="requests")
import requests as r
import json

ReqData = r.get("https://hkolds.vercel.app/api/v1/version")

data = json.loads(ReqData.text)
version = data['projectVersion']
state = data['status']
print(f"O Projeto está na versão {version} e com status em {state}")