import utime
import LCD
from colour import colour

# Configuração do display
display = LCD.LCD_1inch3()

# Define a cor rosa pink
red_color = colour(255, 0, 0)  # RGB para red 
green_color = colour(127, 255, 0)

# Preenche o fundo do display com preto
display.fill(colour(0, 0, 0))

# Exibe o texto em múltiplas linhas
display.printstring('FORA', 24, 20, 3, 0, 0, red_color)   # Primeira linha
display.printstring('Ricardo!', 24, 50, 3, 0, 0,green_color)    # Segunda linha
display.printstring(' ', 24, 80, 3, 0, 0, red_color)             # Linha vazia (espaço)
display.printstring('#destituicao', 24, 110, 3, 0, 0, red_color)       # Quarta linha, ajustada para não sobrepor

# Atualiza o display para mostrar o texto
display.show()
