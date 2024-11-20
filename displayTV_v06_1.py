import utime
import LCD
from colour import colour

# Configuração do display
display = LCD.LCD_1inch3()

# Define as cores
red_color = colour(255, 0, 0)  # RGB para vermelho
green_color = colour(127, 255, 0)  # RGB para verde

# Função para exibir o texto com movimento de letreiro
def letreiro(textos, cores, tamanho_fonte=3, delay=0.05):
    largura_display = 240  # Ajuste conforme necessário para o seu display
    altura_display = 240   # Ajuste conforme necessário para o seu display
    x_inicial = largura_display  # Começa fora do lado direito do display

    # Definir as margens para centralizar verticalmente
    linha_em_branco_antes = 2  # Linhas em branco antes de exibir o texto

    while True:
        # Limpa a tela antes de atualizar
        display.fill(colour(0, 0, 0))

        # Exibe cada linha de texto com as cores e o cálculo para centralizar
        for i, (texto, cor) in enumerate(zip(textos, cores)):
            # Estima a largura do texto com base no número de caracteres e no tamanho da fonte
            texto_largura = len(texto) * tamanho_fonte * 6  # A largura média de cada caractere com tamanho de fonte 3
            x_centralizado = (largura_display - texto_largura) // 2  # Calcula a posição para centralizar o texto

            # Ajusta a posição vertical com base no tamanho da fonte e adiciona linhas em branco
            y = (linha_em_branco_antes * tamanho_fonte * 10) + 20 + i * (tamanho_fonte * 10)

            # Exibe o texto na posição calculada
            display.printstring(texto, x_centralizado + x_inicial, y, tamanho_fonte, 0, 0, cor)

        # Atualiza o display
        display.show()

        # Move o texto para a esquerda
        x_inicial -= 8  # Ajuste a velocidade do letreiro

        # Reinicia o movimento quando o texto sai da tela
        if x_inicial < -largura_display:
            x_inicial = largura_display

        # Aguarda um pouco antes de atualizar
        utime.sleep(delay)

# Lista de textos e cores para cada linha
textos = ["FORA", "Ricardo!"]
cores = [red_color, green_color]

# Executa o letreiro com os textos e cores definidos
letreiro(textos, cores, tamanho_fonte=3)
