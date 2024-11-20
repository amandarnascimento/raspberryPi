import utime
import LCD
from colour import colour

# Configuração do display
display = LCD.LCD_1inch3()

# Define a cor rosa pink
pink_color = colour(255, 105, 180)  # RGB para rosa pink

# Função para exibir o texto com movimento de letreiro
def letreiro(textos, cor, delay=0.05):
    largura_display = 240  # Ajuste conforme necessário para o seu display
    x_inicial = largura_display  # Começa fora do lado direito do display

    while True:
        # Limpa a tela antes de atualizar
        display.fill(colour(0, 0, 0))
        
        # Exibe cada linha de texto na posição x atual
        for i, texto in enumerate(textos):
            y = 20 + i * 30  # Posiciona as linhas com espaçamento vertical
            display.printstring(texto, x_inicial, y, 3, 0, 0, cor)

        # Atualiza o display
        display.show()

        # Move o texto para a esquerda
        x_inicial -= 5  # Ajuste a velocidade do letreiro

        # Reinicia o movimento quando o texto sai da tela
        if x_inicial < -largura_display:
            x_inicial = largura_display

        # Aguarda um pouco antes de atualizar
        utime.sleep(delay)

# Lista de textos para exibir em diferentes linhas
textos = ["FORA", "RICARDO!", " ", "#adios"]

# Executa o letreiro com o texto em rosa pink
letreiro(textos, pink_color)
