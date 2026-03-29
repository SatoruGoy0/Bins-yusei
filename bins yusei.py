import random
import os
import time
from datetime import datetime

# Intentar importar pyfiglet para el banner masivo
try:
    import pyfiglet
except ImportError:
    pyfiglet = None

# Ghostface ASCII con un toque más oscuro
GHOSTFACE = r"""
           .-----------.
          /             \
         |   ()     ()   |
          \      ^      /
           \    |||    /
            \   |||   /
             '-------'
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def luhn_checksum(number):
    digits = [int(d) for d in str(number)]
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def generate_full_card(bin_prefix):
    # Generar número
    card_num = str(bin_prefix).lower().replace("x", "")
    while len(card_num) < 15:
        card_num += str(random.randint(0, 9))
    
    for i in range(10):
        if luhn_checksum(card_num + str(i)):
            card_num += str(i)
            break
    else: card_num += "0"

    # Fecha y CVV
    month = f"{random.randint(1, 12):02d}"
    year = str(random.randint(2026, 2031)) # Basado en año actual 2026
    cvv = f"{random.randint(100, 999)}"
    
    return f"{card_num}|{month}|{year}|{cvv}"

def main():
    clear_screen()
    
    # Imprimir Ghostface primero
    print(GHOSTFACE)

    # Banner Yusei estilo "Minecraft/Block"
    if pyfiglet:
        # La fuente 'block' es la que mejor imita el estilo de cubos/grande
        banner = pyfiglet.figlet_format("YUSEI", font="block")
        print(banner)
    else:
        print("\n[!] Instala pyfiglet para ver el banner estilo Minecraft\n")

    print("=" * 60)
    print("        GHOSTFACE BIN GENERATOR - BY YUSEI")
    print("=" * 60)

    try:
        bin_input = input("\n[?] Ingresa el BIN (6-10 dígitos): ")
        cantidad = input("[?] ¿Cuántas tarjetas quieres? (Enter para 10): ")
        cantidad = int(cantidad) if cantidad.isdigit() else 10

        print(f"\n[+] Generando {cantidad} tarjetas con éxito...\n")
        time.sleep(0.5)

        for _ in range(cantidad):
            print(f" > {generate_full_card(bin_input)}")
        
        print("\n" + "=" * 60)
        print("  Generación completada. ¿Deseas hacer otra?")
        
    except KeyboardInterrupt:
        print("\n\n[!] Operación cancelada.")
    except Exception as e:
        print(f"\n[!] Ocurrió un error: {e}")

if __name__ == "__main__":
    main()