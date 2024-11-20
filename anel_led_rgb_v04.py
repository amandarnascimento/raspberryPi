import machine
import utime
from ws2812 import WS2812

# Declaração do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)

# Laço de execução alternando entre vermelho e azul
while True:
    # Define a cor vermelha para todos os LEDs
    for i in range(12):
        ws[i] = [255, 0, 255]  # Vermelho
    ws.send()
    utime.sleep(1)  # Espera 2 segundos

    # Define a cor azul para todos os LEDs
    for i in range(12):
        ws[i] = [0, 0, 255]  # Azul
    ws.send()
    utime.sleep(5)  # Espera 2 segundos
