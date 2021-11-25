import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5

player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aidahardy tamaqtandyru")

# images
background = pygame.image.load('background.png')

score_backround = pygame.image.load('score_background.png').convert_alpha()
score_background_rect = score_backround.get_rect()
score_background_rect.topleft = (10,10)

live_background = pygame.image.load('score_background.png').convert_alpha()
live_background_rect = live_background.get_rect()
live_background_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width+10), 10)

dragon_image = pygame.image.load('dragon.png').convert_alpha()
dragon_image = pygame.transform.rotate(dragon_image, 90)
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (80, WINDOW_HEIGHT//2)

bird_image = pygame.image.load('bird.png').convert_alpha()
bird_image_rect = bird_image.get_rect()
bird_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))

# fonts and texts
main_font = pygame.font.Font('AttackGraffiti.ttf', 32)

score_text = main_font.render("Upai: " + str(player_score), True, RED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (20, 20)

game_name = main_font.render("Aidahardy Tamaqtandyru", True, RED, WHITE)
game_name_rect = game_name.get_rect()
game_name_rect.center = (WINDOW_WIDTH//2, HEADER_HEIGHT//2)

live_text = main_font.render("Jany: " + str(player_live), True, RED)
live_text_rect = live_text.get_rect()
live_text_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width), 20)

# sounds and musics
pygame.mixer.music.load('music.wav')
sound1 = pygame.mixer.Sound('sound_1.wav')
sound2 = pygame.mixer.Sound('sound_2.wav')

FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.play(-1, 0.0)
# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(background, (0,0))
    display_surface.blit(score_backround, score_background_rect)
    display_surface.blit(live_background, live_background_rect)
    pygame.draw.line(display_surface, WHITE, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT), 5)
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(bird_image, bird_image_rect)
    
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(game_name, game_name_rect)
    display_surface.blit(live_text, live_text_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()