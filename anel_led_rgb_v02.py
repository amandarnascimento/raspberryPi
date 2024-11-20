import machine
import utime
import urandom
from ws2812 import WS2812

# Declaração do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)

# Lista de cores predefinidas (vermelho, verde, azul, amarelo, ciano, magenta, branco)
cores = [
    [255, 0, 0],     # Vermelho
    [0, 255, 0],     # Verde
    [0, 0, 255],     # Azul
    [255, 255, 0],   # Amarelo
    [0, 255, 255],   # Ciano
    [255, 0, 255],   # Magenta
    [255, 255, 255]  # Branco
]

# Laço de execução
while True:
    # Itera no Anel de LEDs passando o valor(cor) do LED i para o LED i-1
    for i in range(11, 0, -1):
        ws[i] = ws[i - 1]

    # Seleciona uma cor aleatória da lista de cores
    ws[0] = cores[urandom.randint(0, len(cores) - 1)]

    # Envia a informação para o Anel de LEDs
    ws.send()

    utime.sleep_ms(80)
