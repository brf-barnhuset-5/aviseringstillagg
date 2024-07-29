import datetime
import json
import requests

from config import config

s = requests.Session()

r = s.post(
  url='https://portal.simpleko.se/api/auth/login',
  json={
    'username': config['credentials']['username'],
    'password': config['credentials']['password'],
  },
)

now = datetime.datetime.now()

simpleko_apartments = s.get('https://portal.simpleko.se/api/portal/customerInvoices/extra-costs').json()

simpleko_apartments = {
  x['objectLabel']: x['objectId']
  for x in simpleko_apartments['data']['realEstates']
}

fh = open('addons.json', 'r')
addons = json.loads(fh.read())
fh.close()

try:
  for apartment in addons:
    for addon in addons[apartment]:
      if 'added' in addon and addon['added']:
        continue

      addon_date = datetime.datetime.strptime(addon["date"], '%Y-%m-%d')

      if now >= addon_date:
        apartment_id = config['apartment_mapping'][apartment] if 'apartment_mapping' in config else apartment

        r = s.post('https://portal.simpleko.se/api/portal/customerInvoices/extra-costs/' + str(simpleko_apartments[apartment_id]), json={
          "subject": addon["description"],
          "amount": str(addon["amount"]),
          "category": "3542",
        })

        if r.ok:
          addon['added'] = True

except Exception as e:
  print(e)

fh = open('addons.json', 'w')
addons = fh.write(json.dumps(addons, indent=2))
fh.close()
