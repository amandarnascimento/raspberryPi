# Codigo 6.3 - Teclado de Cores
 
 
 
 
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
 
 
 
 
# Declaracao das variaveis
 
 
 
 
estado_botao_1 = 0
 
estado_botao_2 = 0
 
estado_botao_3 = 0
 
estado_botao_4 = 0
 
azul_ligado = False
 
branco_ligado = False
 
verde_ligado = False
 
vermelho_ligado = False
 
 
 
 
# Laco de execucao
 
 
 
 
while True:
 
     
 
    estado_botao_1 = botao_1.value()
 
    estado_botao_2 = botao_2.value()
 
    estado_botao_3 = botao_3.value()
 
    estado_botao_4 = botao_4.value()
 
    if estado_botao_1 == 1:
 
        if not vermelho_ligado:
 
            ws.write_all(0xFF0000)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = True
 
        else:
 
            ws.write_all(0x000000)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = False
 
    elif estado_botao_2 == 1:
 
        if not verde_ligado:
 
            ws.write_all(0x00FF00)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = True
 
            vermelho_ligado = False
 
        else:
 
            ws.write_all(0x000000)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = False
 
    elif estado_botao_3 == 1:
 
        if not azul_ligado:
 
            ws.write_all(0x0000FF)
 
            azul_ligado = True
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = False
 
        else:
 
            ws.write_all(0x000000)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = False
 
    elif estado_botao_4 == 1:
 
        if not branco_ligado:
 
            ws.write_all(0xFFFFFF)
 
            azul_ligado = False
 
            branco_ligado = True
 
            verde_ligado = False
 
            vermelho_ligado = False
 
        else:
 
            ws.write_all(0x000000)
 
            azul_ligado = False
 
            branco_ligado = False
 
            verde_ligado = False
 
            vermelho_ligado = False
 
    utime.sleep(0.2)
