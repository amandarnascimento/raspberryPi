import machine
import utime
from ws2812 import WS2812

# Declaração do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)

# Função para aumentar ou diminuir gradualmente o brilho de uma cor
def fade_color(start_color, end_color, steps):
    for step in range(steps):
        color = [
            start_color[i] + (end_color[i] - start_color[i]) * step // steps
            for i in range(3)
        ]
        for j in range(12):
            ws[j] = color
        ws.send()
        utime.sleep_ms(50)

# Laço de execução alternando entre cores
while True:
    fade_color([255, 0, 0], [0, 0, 255], 50)  # De vermelho para azul
    fade_color([0, 0, 255], [0, 255, 0], 50)  # De azul para verde
    fade_color([0, 255, 0], [255, 255, 0], 50)  # De verde para amarelo
    fade_color([255, 255, 0], [255, 0, 0], 50)  # De amarelo para vermelho
