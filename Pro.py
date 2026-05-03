import requests
import time

# En nivel pro, usamos la API (requiere una API Key de 3.50$)
# O simulamos la petición si es para fines educativos
API_KEY = "tu_api_key_aqui"
headers = {
    "hibp-api-key": API_KEY,
    "user-agent": "Email-Checker-Pro"
}

def check_email(email):
    url = f"https://haveibeenpwned.com{email}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return f"[!] {email} ha sido vulnerado."
        elif response.status_code == 404:
            return f"[+] {email} está a salvo."
        elif response.status_code == 429:
            return "[-] Error: Demasiadas peticiones. Esperando..."
    except Exception as e:
        return f"[-] Error de conexión: {e}"

# Leer y procesar de forma eficiente
with open('escribir_correos.txt', 'r') as f:
    emails = f.read().splitlines()

print(f"[*] Iniciando escaneo de {len(emails)} correos...\n")

for email in emails:
    resultado = check_email(email)
    print(resultado)
    # Guardar en un log automáticamente
    with open('resultados.log', 'a') as log:
        log.write(resultado + "\n")
    
    # Respetar el límite de la API
    time.sleep(1.5) 
