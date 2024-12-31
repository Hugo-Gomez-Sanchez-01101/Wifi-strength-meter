import os
import time
import re
import platform
from colorama import Fore, init

init(autoreset=True)

def get_wifi_signal_strength():
    system = platform.system()
    try:
        if system == "Windows":
            result = os.popen('netsh wlan show interfaces').read()
            for line in result.splitlines():
                if re.search(r"Se.*al", line):
                    return int(re.search(r"\d+", line.split(":")[1]).group())
        elif system == "Linux":
            result = os.popen('nmcli -t -f IN-USE,SIGNAL dev wifi').read()
            for line in result.splitlines():
                if line.startswith("*"):
                    return int(line.split(":")[1])
        else:
            print("Sistema operativo no compatible.")
            return None
    except Exception as e:
        print(f"Error al obtener la intensidad de la señal: {e}")
        return None

def get_color_for_signal(strength):
    if strength < 25:
        return Fore.RED
    elif 25 <= strength < 50:
        return Fore.LIGHTRED_EX
    elif 50 <= strength < 75:
        return Fore.YELLOW
    else:
        return Fore.LIGHTGREEN_EX

def draw_signal_bar(strength):
    bar_length = 30
    filled_length = int(bar_length * strength / 100)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    color = get_color_for_signal(strength)
    print(f"\r{color}[{bar}] {strength}%{' ' * 10}", end="")

def locate_router():
    print("Localizando el router... Presiona Ctrl+C para detener el escaneo.")
    try:
        while True:
            signal_strength = get_wifi_signal_strength()
            if signal_strength is not None:
                draw_signal_bar(signal_strength)
            else:
                print("\rNo se pudo obtener la intensidad de la señal. Verifica tu conexión WiFi.", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nEscaneo detenido.")

if __name__ == "__main__":
    locate_router()
