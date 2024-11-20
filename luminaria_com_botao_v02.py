# Codigo 6.2 - Ligando luminária com botão

# Bibliotecas necessárias para o código
import machine
import utime

# Importação das bibliotecas customizadas 
from ws2812 import WS2812

# Declaração do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)

# Declaração dos botões
botao_1 = machine.Pin(18, machine.Pin.IN)
botao_2 = machine.Pin(19, machine.Pin.IN)
botao_3 = machine.Pin(20, machine.Pin.IN)
botao_4 = machine.Pin(21, machine.Pin.IN)

# Declaração das variáveis do código
estado_botao_1 = 0
estado_botao_2 = 0
estado_botao_3 = 0
estado_botao_4 = 0

# Laço de execução
while True:

    estado_botao_1 = botao_1.value()
    estado_botao_2 = botao_2.value()
    estado_botao_3 = botao_3.value()
    estado_botao_4 = botao_4.value()

    if estado_botao_1 == 1:
        ws.write_all(0x444444)  # Cor para o botão 1 (cinza escuro)
    elif estado_botao_2 == 1:
        ws.write_all(0x888888)  # Cor para o botão 2 (cinza)
    elif estado_botao_3 == 1:
        ws.write_all(0xFF00FF)  # Cor rosa para o botão 3 (pink)
    elif estado_botao_4 == 1:
        ws.write_all(0x000000)  # Cor para o botão 4 (desligado)

    utime.sleep(0.01)
