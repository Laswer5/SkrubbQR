import requests
import json
import argparse

def generate_qr_code(sekt, format, amount, amount_editable, message, message_editable, size, border, transparent):
    url = "https://mpc.getswish.net/qrg-swish/api/v1/prefilled"
    sekt_dict = {"KV": "1235780887", "IT": "1236130983", "SKRUBB": "1233273281"}

    if sekt not in sekt_dict:
        print("Ogiltigt mottagarkonto")
        return
    
    sekt = sekt_dict[sekt]
    
    # Construct the request body
    payload = {
        "format": format,
        "payee": {
            "value": sekt,
            "editable": False
        },
        "amount": {
            "value": amount,
            "editable": amount_editable
        },
        "message": {
            "value": message,
            "editable": message_editable
        },
        "size": size,
        #"border": border,
        "transparent": transparent
    }

    print(payload)
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        # Save the response as a PNG file
        with open("qr_code.png", "wb") as f:
            f.write(response.content)
        print("QR-kod sparad som qr_code.png")
    else:
        print(f"Misslyckades att generera QR-kod: {response.status_code}, {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generera QR-kod med Swish API")
    
    parser.add_argument("--sekt", required=True, help="KV/IT/SKRUBB")
    
    parser.add_argument("--format", required=True, help="png/jpg/svg")

    parser.add_argument("--amount", required=False, type=float, help="Betalningsbelopp")
    parser.add_argument("--amount_editable", required=False, default=True, type=bool, help="Betalningsbelopp redigerbart? (default: True)")

    parser.add_argument("--message", required=False, help="Betalningsmeddelande")
    parser.add_argument("--message-editable", required=False, default=True, type=bool, help="Betalningsmeddelande redigerbart? (default: True)")

    parser.add_argument("--size", required=False, default=300, type=int, help="Storlek på QR-kod (x*x px)")
    parser.add_argument("--border", required=False, default=0, type=int, help="Kantbredd (px)")
    parser.add_argument("--transparent", required=False, default=True, type=bool, help="Transparent background (ej med jpg)")
    
    args = parser.parse_args()
    
    generate_qr_code(args.sekt, args.format, args.amount, args.amount_editable, args.message, args.message_editable, args.size, args.border, args.transparent)