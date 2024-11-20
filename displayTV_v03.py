import utime
import LCD
from colour import colour

# Configuração do display
display = LCD.LCD_1inch3()

# Define a cor rosa pink
pink_color = colour(255, 105, 180)  # RGB para rosa pink

# Preenche o fundo do display com preto
display.fill(colour(0, 0, 0))

# Exibe o texto em múltiplas linhas
display.printstring('joao', 24, 20, 3, 0, 0, pink_color)   # Primeira linha
display.printstring('te amo!', 24, 50, 3, 0, 0, pink_color)    # Segunda linha
display.printstring(' ', 24, 80, 3, 0, 0, pink_color)             # Linha vazia (espaço)
display.printstring('muitao', 24, 110, 3, 0, 0, pink_color)       # Quarta linha, ajustada para não sobrepor

# Atualiza o display para mostrar o texto
display.show()
