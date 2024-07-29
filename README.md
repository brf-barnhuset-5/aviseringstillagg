# aviseringstillägg
Detta skript låter dig lägga upp schemalagda avseringstillägg i portalen hos Simpleko. Behovet finns då löpande aviseringstillägg inte kan läggas upp direkt i portalen. Specificera tilläggen i en JSON-fil och schemalägg skriptet att köras, till exempel en gång per dag.

## Installation och användning
1. Kopiera `config.example.py` till `config.py` och fyll i dina inloggningsuppgifter till Simplekos portal.
2. Kopiera `addons.example.json` till `addons.json` och fyll i de averingeringstillägg som ska göras. Ange lägenhetsnummer, beskrivning och datum för när tillägget som tidigast ska läggas till. Se nedan angående formen på lägenhetsnummer.
3. Sätt upp en Python-miljö och installera nödvändiga Python-paket:
   ```
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip3 install -r requirementst.txt
   ```
4. Kör skriptet:
   ```
   $ source venv/bin/activate
   $ python3 main.py
   ```
5. Schemalägg så att skriptet körs en gång per dygn, till exempel klockan 00.30.

## Översättning av lägenhetsnummer
I den här föreningen används genomgående det fyrsiffriga lägenhetsnumret, men Simpleko har ändå insisterat på att använda det tresiffriga lägenhetsnumret i sitt system. Av det skälet behövs en översättning, och en sådan kan ses i `config.py`. Justera den, `apartment_mapping`, för att passa dina lägenhetsnummer. Om du inte vill göra någon översättning, ta bort `apartment_mapping` helt. Du får då ange lägenhetsnummer i `addons.json` på samma form som de är skrivna i Simplekos system.

## Förhindra duplicering av tillägg
Skriptet lägger till ett fält och ett värde i `addons.json`, `"added": true`, när det har lagt till ett aviseringstillägg. Det gör att tillägg inte dupliceras. För att detta ska fungera är det dock viktigt att skriptet har både läs- och skrivåtkomst till `addons.json` när det körs.
