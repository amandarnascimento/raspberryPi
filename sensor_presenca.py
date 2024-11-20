# Codigo 7.2 - Detector de movimento
 
 
 
 
# Bibliotecas necessarias para o codigo
 
 
 
 
# Importacao das bibliotecas padrao
 
 
 
 
import machine
 
import utime
 
 
 
 
# Declaracao do sensor PIR
 
 
 
 
sensor_pir = machine.Pin(19, machine.Pin.IN)
 
 
 
 
# Declaracao do LED
 
 
 
 
led = machine.Pin(15,machine.Pin.OUT)
 
 
 
 
# Declaracao das variaveis do codigo
 
 
 
 
movimento = False
 
 
 
 
# Funcao a ser chamada quando houver uma borda positiva no pino do sensor PIR
 
 
 
 
def movimento_detectado(_):
 
     
 
    global movimento
 
    movimento = True
 
     
 
# Declaracao da interrupcao no pino do sensor PIR
 
 
 
 
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=movimento_detectado)
 
 
 
 
# Laco de execucao
 
 
 
 
while True:
 
     
 
    if movimento:
 
        led.value(1)
 
        print("Alguem passou aqui!")
 
        utime.sleep(3)
 
        led.value(0)
 
        movimento = False