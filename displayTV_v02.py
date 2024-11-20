import utime
import LCD
from colour import colour

# Configuração do display
display = LCD.LCD_1inch3()

# Função para criar o efeito de letreiro rápido
def scroll_text(text, y, speed=0.02, step=3, color=(0, 255, 0)):
    text_length = len(text) * 8  # Aproximadamente 8 pixels por caractere (ajuste se necessário)
    display_width = 240          # Substitua pelo valor da largura do seu display se for diferente

    while True:
        for x in range(display_width, -text_length, -step):  # Move o texto com passos maiores
            display.fill(colour(0, 0, 0))                    # Limpa o fundo
            display.printstring(text, x, y, 3, 0, 0, colour(*color))
            display.show()
            utime.sleep(speed)  # Menor valor para maior velocidade

# Executa a função de letreiro rápido com a mensagem desejada
scroll_text('Oi, olivia te amo!', y=30, speed=0.02, step=5)
