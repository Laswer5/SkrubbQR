# SkrubbQR

Detta Python-skript kan användas för att generera en QR-kod för Swish-betalningar till IT-Sektionen/Klubbverk/Skrubben. Skriptet använder Swish API:et för att skapa en QR-kod med specifika detaljer som mottagare, belopp, meddelande m.m.

### Användning
## Exempel
```bash
python SkrubbQR.py --sekt KV --format png --amount 30 --message "pubrundemärke" --size 600 --transparent true
```

### Installation

Installera requests, json, och argparse med valfri pakethanterare om du inte redan har dem.

