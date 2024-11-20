# Codigo 11.2 - Sua mensagem no display
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import utime
 
# Importacao das bibliotecas customizadas 
 
import LCD
from colour import colour
 
# Declaracao do LCD
 
display = LCD.LCD_1inch3()
 
# Preenche o fundo do display com preto e escreve 'Oi, mundo!' em verde partindo das coordenadas 20 px e 10 px
 
display.fill(colour(0,0,0))
display.printstring('Oi, olivia te amo!',24,30,3,0,0,colour(0,255,0))
display.show()