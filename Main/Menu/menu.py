import os
import constantes
import pygame

class Jogo:
    def __init__(self):
        # Criando Tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.carregar_arquivos()

    def carregar_arquivos(self):
        # Carregar os arquivos de áudio e imagens
        diretorio_imagem = os.path.join(os.getcwd(), "Main/Menu")
        self.diretorio_audios = os.path.join(os.getcwd(), 'Main/Sons')
        
        # Caminho completo para a imagem do logo
        caminho_logo = os.path.join(diretorio_imagem, constantes.BOMBERMAN_START_LOGO)
        
        # Verificação se o arquivo de imagem existe
        if not os.path.isfile(caminho_logo):
            raise FileNotFoundError(f"Arquivo de imagem não encontrado: {caminho_logo}")
        
        self.bomberman_start_logo = pygame.image.load(caminho_logo).convert()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        # Exibe texto inicial
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)
    
    def mostrar_start_logo(self,x,y):
        start_logo_rect = self.bomberman_start_logo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.bomberman_start_logo, start_logo_rect)


    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantes.MUSICA_MENU))
        pygame.mixer_music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        self.mostrar_start_logo(370 , -100)
        self.mostrar_texto('-Pressione uma tecla para jogar', 32, constantes.BRANCO, 390, 450)
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYDOWN:
                    esperando = False
                    pygame.mixer_music.stop()
                    pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantes.CLIQUE_MENU))
                    pygame.mixer_music.set_volume(1)
                    pygame.mixer.music.play()


menu = Jogo()
menu.mostrar_tela_start()