from machine import Pin
import time

# Configura o LED embutido do Raspberry Pi Pico (geralmente no pino 25)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)  # Liga o LED
    time.sleep(0.5)  # Espera 0,5 segundos
    led.value(0)  # Desliga o LED
    time.sleep(0.5)  # Espera 0,5 segundos
