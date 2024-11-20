# Codigo 6.2 - Ligando luminaria com botao
 
 
# Bibliotecas necessarias para o codigo
 
 
# Importacao das bibliotecas padrao
 
 
import machine
 
import utime
 
 
# Importacao das bibliotecas customizadas 
 
 
from ws2812 import WS2812
 
 
# Declaracao do Anel de LEDs
 
 
ws = WS2812(machine.Pin(28), 12)
 
 
# Declaracao dos botoes
 
 
botao_1 = machine.Pin(18, machine.Pin.IN)
 
botao_2 = machine.Pin(19, machine.Pin.IN)
 
botao_3 = machine.Pin(20, machine.Pin.IN)
 
botao_4 = machine.Pin(21, machine.Pin.IN)
 
 
# Declaracao das variaveis do codigo
 
estado_botao_1 = 0
 
estado_botao_2 = 0
 
estado_botao_3 = 0
 
estado_botao_4 = 0
 
 
# Laco de execucao
 
 
while True:
 
     
    estado_botao_1 = botao_1.value()
 
    estado_botao_2 = botao_2.value()
 
    estado_botao_3 = botao_3.value()
 
    estado_botao_4 = botao_4.value()
 
    if estado_botao_1 == 1:
 
        ws.write_all(0x444444)
 
    elif estado_botao_2 == 1:
 
        ws.write_all(0x888888)
 
    elif estado_botao_3 == 1:
 
        ws.write_all(0xFFFFFF)
 
    elif estado_botao_4 == 1:
 
        ws.write_all(0x000000)
 
    utime.sleep(0.01)