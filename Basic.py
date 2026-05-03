import webbrowser
import time
import pyperclip
import pyautogui

# Abrimos el archivo y cargamos los correos en una lista
documento = open('escribir_correos.txt', 'r')
documento = documento.read().split('\n')

# Ahora aquí ordenamos que se escriba con el teclado:

for email in documento:
    # Abre la web en una pestaña nueva
    webbrowser.open_new_tab("https://haveibeenpwned.com")
    
    # Esperamos 3 segundos a que cargue la página (Ajusta si tu internet es lento)
    time.sleep(3)

    # Copiamos el email actual al portapapeles
    pyperclip.copy(email) 

    # Pegamos el email usando el atajo Ctrl+V
    # El interval=0.15 añade un pequeño retraso para que sea más humano
    pyautogui.hotkey('ctrl', 'v', interval=0.15) 

    # Pulsamos Enter para iniciar la búsqueda
    pyautogui.press("enter")
    
    # Opcional: podrías añadir un time.sleep(2) aquí si quieres ver el resultado 
    # antes de que abra la siguiente pestaña.
