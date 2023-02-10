import pygame, sys, random, time, math

clock = pygame.time.Clock()

#textos 
pygame.font.init()
fonte = pygame.font.get_default_font()
fonte_jogo = pygame.font.SysFont('impact', 400)
fonte_subtexto = pygame.font.SysFont (fonte, 75)
fonte_tempo = pygame.font.SysFont (fonte, 40)
fonte_tempo_final = pygame.font.SysFont (fonte, 100)

pygame.mixer.init()


""" inicial = fonte_jogo.render("Altitude", True, (221, 110, 9))
inicial_rect = inicial.get_rect()
inicial_rect.center = (1600//2, 600//2)


subtx_inicial = fonte_subtexto.render ('Aperte ESPAÇO para jogar', True, (255,255,255))
subtx_incial_rect = subtx_inicial.get_rect()
subtx_incial_rect.center = (1600//2, 500)

perdeu = fonte_jogo.render('Game Over', True, (221, 110, 9))
perdeu_rect = perdeu.get_rect()
perdeu_rect.center = (1600//2, 600//2)

ganhou = fonte_jogo.render('You Win', True, (23, 69, 78))
ganhou_rect = ganhou.get_rect()
ganhou_rect.center = (1600//2, 600//2)

jogarnov = fonte_subtexto.render('Aperte ESC para jogar novamente', True, (255,255,255))
jogarnov_rect = jogarnov.get_rect()
jogarnov_rect.center = (1600//2, 500) """
#imagens

incio = pygame.image.load('inicio.png')
ganhou = pygame.image.load ('ganhou.png')
perdeu = pygame.image.load('perdeu.png')
ibex = pygame.image.load('ibex.png')

#sons
musica_abertura = 1
#abertura_som = pygame.mixer.music.load('abertura-som.mp3')
#ganhou_som = pygame.mixer.music.load('ganhou-som.mp3')
#perdeu_som = pygame.mixer.music.load('perdeu-som.mp3')
#jogando_som = pygame.mixer.music.load('jogando-musica.mp3')

#variaveis
cor_r_margens = pygame.Color (221, 141, 57)
cor_r_meio = pygame.Color (221, 110, 9)
cor_boneco = pygame.Color (23, 69, 78)
cor_reboco = pygame.Color (221, 110, 9)

retangulo_inicial = pygame.Rect(0,300,40,300)
retangulo_final = pygame.Rect(1560,300,40,300)
reboco = pygame.Rect(40, 570, 1520, 30)
pygame.init()

#tela 
tela = pygame.display.set_mode((1600, 600))
pygame.display.set_caption('Altitude')

fundo = pygame.image.load('backred.png').convert()
largura_fundo = fundo.get_width()

scroll = 0
tiles = math.ceil(1600/largura_fundo)




while True:



    altitudes = []
    coluna_atual = 0
    for i in range (40):
        altitudes.append(random.randrange(50, 550, 10))
    xdoboneco = 0


    #tela.fill((115, 16, 182))
    #tela.blit (inicial, inicial_rect)
    #tela.blit(subtx_inicial, subtx_incial_rect)
    
    tela.blit (incio, (0,0))
    rodando = False
    inicio = True


    if inicio:  
        pygame.display.flip()  
        clock.tick(60)  
        if musica_abertura == 1:
            pygame.mixer.music.load('abertura-som.mp3')
            pygame.mixer.music.play(loops=-1, fade_ms=1)
            musica_abertura = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inicio = False
                    rodando = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()

    esperando = True

    tempora = 0
    musica_jogo = 1
    #Logica do jogo
    while rodando:
        clock.tick(60)
        tempo_final = fonte_tempo_final.render(f'{tempora:.1f}s', True, (255,255,255))
        tempo_final_rect = tempo_final.get_rect()
        tempo_final_rect.center = (1600//2, 100)

        cronometro = f'TIME = {tempora:.1f}'
        tempo = fonte_tempo.render(cronometro, True, (255,255,255))
        tempo_rect = tempo.get_rect()
        tempo_rect.center = (1480, 20)

        
        if musica_jogo == 1:
            jogando_som = pygame.mixer.music.load('jogando-musica.mp3')
            pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
            musica_jogo = 0
        #rolagem da tela
        for i in range (0, tiles):
            tela.blit(fundo, ( i * largura_fundo + scroll,0))

        scroll -= 5

        if abs(scroll) > largura_fundo:
            scroll = 0
        
        if coluna_atual == 38:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('ganhou-som.mp3')
            pygame.mixer.music.play()
            """ tela.blit(ganhou, ganhou_rect)
            tela.blit (jogarnov, jogarnov_rect) """
            tela.blit(ganhou,(0,0))
            tela.blit(tempo_final, tempo_final_rect)
            pygame.display.flip()       
            esperando = True     
            while esperando:
                clock.tick(60)  
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        esperando = False
                        rodando = False
                        inicio = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            esperando = False
                            rodando = False
                            inicio = True
                            pygame.mixer.music.unload()
                            musica_abertura = 1
                                            
                        
        #movimentação das colunas e boneco
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    altitudes[coluna_atual] += 10
                
                elif event.key == pygame.K_DOWN:
                    altitudes[coluna_atual] -= 10

                elif event.key == pygame.K_RIGHT:
                    if altitudes[coluna_atual] == 300:
                        xdoboneco += 40
                        #if coluna_atual < 37:
                        coluna_atual += 1
                    else:       
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load('perdeu-som.mp3')
                        pygame.mixer.music.play()
                        """ tela.blit(perdeu, perdeu_rect)
                        tela.blit (jogarnov, jogarnov_rect) """
                        tela.blit(perdeu, (0,0))
                        tela.blit(tempo_final, tempo_final_rect)
                        pygame.display.flip()       
                        esperando = True     
                        while esperando:
                            clock.tick(60)  
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        esperando = False
                                        rodando = False
                                        sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                            pygame.mixer.music.unload()
                                            esperando = False
                                            rodando = False
                                            inicio = True
                                            pygame.mixer.music.unload()
                                            musica_abertura = 1
                                            
        
            
        pygame.draw.rect(tela, cor_r_margens, retangulo_inicial)
        boneco = pygame.Rect(xdoboneco, 260, 40, 40)
        tela.blit(ibex, boneco)
        
        if coluna_atual == 0:
            preenchidas = coluna_atual
        else:
            preenchidas = coluna_atual -1
    

        for i in range (preenchidas, 38):
            repeticoes = random.randrange(-3, 3, 2)
            retangulo_prox = pygame.Rect((i + 1) * 40, 600 - altitudes[i], 40, altitudes[i] + repeticoes*10 )
            pygame.draw.rect(tela, cor_r_meio, retangulo_prox) 
        pygame.draw.rect(tela, cor_r_margens, retangulo_final)
        pygame.draw.rect(tela, cor_reboco, reboco)
        tela.blit (tempo, tempo_rect)

        
        lista = []
        tempora = tempora + 0.016
    

        

        pygame.display.update()

        