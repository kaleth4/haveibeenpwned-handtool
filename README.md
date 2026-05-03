```markdown
# **Have I Been Pwned? - Automatizador Pro vs. Amateur**

## 📌 **Descripción General**
Esta herramienta automatiza la verificación de correos electrónicos en [Have I Been Pwned](https://haveibeenpwned.com), comparando dos enfoques:
- **Nivel Amateur**: Simula interacción humana con `pyautogui` (útil para pruebas rápidas).
- **Nivel Pro**: Usa la API oficial para mayor eficiencia, escalabilidad y precisión.

---

## ✅ **Lo Bueno del Enfoque Amateur**
- **Creatividad**: Evita aprender APIs complejas al emular acciones humanas.
- **Funcionalidad básica**: Funciona bien para listas pequeñas (5-10 correos).

---

## ⚠️ **Problemas del Nivel "Amateur"**
| Problema | Impacto |
|----------|---------|
| **Dependencia del hardware** | Si el internet tarda más de lo esperado (ej. 4s vs 3s), el script falla. Mover el ratón interrumpe la ejecución. |
| **Invisibilidad de resultados** | No guarda registros automáticos; requiere supervisión constante. |
| **Velocidad y recursos** | Abrir pestañas por correo es lento y consume mucha RAM. |

---

## 🚀 **Versión "Nivel Pro" (Recomendada)**
Usa la **API oficial** de Have I Been Pwned para:
✔ **Procesar miles de correos en segundos**
✔ **Ejecutarse en segundo plano** (sin abrir navegador)
✔ **Guardar resultados automáticamente** en `resultados.log`
✔ **Evitar fallos por hardware**

### 📂 **Código Pro (Python)**
```python
import requests
import time

# API Key (opcional: 3.50$ para uso ilimitado)
API_KEY = "tu_api_key_aqui"  # O usa la versión gratuita sin key
headers = {
    "hibp-api-key": API_KEY,
    "user-agent": "Email-Checker-Pro"
}

def check_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
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

# Procesar correos desde archivo
with open('escribir_correos.txt', 'r') as f:
    emails = f.read().splitlines()

print(f"[*] Iniciando escaneo de {len(emails)} correos...\n")

for email in emails:
    resultado = check_email(email)
    print(resultado)
    with open('resultados.log', 'a') as log:
        log.write(resultado + "\n")
    time.sleep(1.5)  # Respetar límites de la API
```

### 🔍 **¿Por qué es mejor?**
| Ventaja | Detalle |
|---------|---------|
| **Resultados reales** | Verifica compromisos reales, no solo simula escritura. |
| **Automatización total** | Ejecuta en segundo plano y guarda logs para revisión posterior. |
| **Estabilidad** | No falla por movimientos del ratón o latencia de red. |

---

## 🛠 **Término Medio: Versión Híbrida (Capturas de Pantalla)**
Si prefieres mantener el enfoque `pyautogui` pero añadir **registros visuales**, aquí tienes el código adaptado para capturar la pantalla antes de cerrar cada pestaña:

```python
import webbrowser
import time
import pyperclip
import pyautogui
from PIL import ImageGrab

# Abrir archivo de correos
with open('escribir_correos.txt', 'r') as f:
    emails = f.read().splitlines()

for email in emails:
    webbrowser.open_new_tab("https://haveibeenpwned.com")
    time.sleep(3)  # Ajustar según tu conexión

    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.press("enter")

    # Capturar pantalla y guardar
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshots/{email}.png")  # Guardar en carpeta 'screenshots'

    # Cerrar pestaña (ajusta según tu sistema operativo)
    pyautogui.hotkey('ctrl', 'w')
```

### 📌 **Notas para la Versión Híbrida**
- **Librerías adicionales**: Instala `Pillow` para capturas:
  ```bash
  pip install pyperclip pyautogui Pillow
  ```
- **Estructura de archivos**: Crea una carpeta `screenshots` en el mismo directorio.
- **Foco del teclado**: Asegúrate de que el cursor esté en el campo de búsqueda de Have I Been Pwned al abrir la pestaña.

---

## 📚 **Recomendación Final**
- **Para uso personal o pruebas**: Usa la versión `pyautogui` con capturas.
- **Para producción o listas grandes**: **Implementa la versión Pro con API** (más eficiente y escalable).

💡 **Tip**: Si no tienes API Key, usa la versión gratuita sin headers (cambia `url` a `
