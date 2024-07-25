import os, pygame

def __init__(self):
    #Criando Tela do jogo
    pygame.init()
    pygame.mixer.init()
    self.tela = pygame.display.set_mode(())

def carregar_arquivos(self):
    #Carregar os arquivos de aúdio e imagens
    diretórioimagem = os.path.join(os.getcwd(), "Menu")
    self.diretorio_audios = os.patch.join(os.getcwd(), 'Sons')
    self.bomberman_start_logo = os.path.join(diretórioimagem, 'Blue and Black Modern Digital Technology Logo.png' )
    self.bomberman_start_logo = pygame.image.load(self.bomberman_start_logo).convert()