import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((900,300))
pygame.display.set_caption("музыка ойнаушы")

playlist = ["lab 7/music player/aot.mp3", "lab 7/music player/jojo.mp3", "lab 7/music player/undertale.mp3", "lab 7/music player/queen.mp3"]

id = 1
pygame.mixer.music.load(playlist[id])
pygame.mixer.music.play()
pygame.mixer.music.pause()

clock = pygame.time.Clock()

bg = pygame.image.load('lab 7/music player/bg.jpg')
bg = pygame.transform.scale(bg, (900, 300))

prev = pygame.image.load('lab 7/music player/prev.png')
play = pygame.image.load('lab 7/music player/play.png')
stop = pygame.image.load('lab 7/music player/stop.png')
next = pygame.image.load('lab 7/music player/next.png')

prev = pygame.transform.scale(prev, (130, 130))
play = pygame.transform.scale(play, (105, 105))
stop = pygame.transform.scale(stop, (100, 120))
next = pygame.transform.scale(next, (130, 130))

done = False
player = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_RIGHT:
                id = (id + 1) % len(playlist) # get the index of the next song
                pygame.mixer.music.stop() # stop the currently playing music
                pygame.mixer.music.load(playlist[id]) # load the next song
                pygame.mixer.music.play() # play the next song
                player = True

            if event.key == pygame.K_LEFT:
                id = (id - 1) % len(playlist)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(playlist[id])
                pygame.mixer.music.play()
                player = True

            elif not player and event.key == pygame.K_SPACE:
                player = True
                pygame.mixer.music.unpause()

            elif player and event.key == pygame.K_SPACE:
                player = False
                pygame.mixer.music.pause()

    font = pygame.font.SysFont(None, 24)     
    screen.blit(bg, (0, 0))
    screen.blit(prev, (150, 160))
    screen.blit(play, (295, 167))
    screen.blit(stop, (425, 159))
    screen.blit(next, (560, 160))
    pygame.display.update()
    clock.tick(60)

pygame.quit()