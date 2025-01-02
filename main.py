##################
# STAR WARS GAME #
##################

# import modules
import pygame
import sys
import random

# pygame initialization
pygame.init()

# screen
screen = pygame.display.set_mode()
screen_width = screen.get_width()
screen_height = screen.get_height()

# images
jedi = pygame.image.load("assets/jedi.png")
jedi_rect = jedi.get_rect()
jedi_rect.center = (screen_width // 2, screen_height // 2)

text_size = 30 # because I need it now

sith = pygame.image.load("assets/sith.png")
sith_rect = sith.get_rect()
sith_rect.topleft = (0, text_size * 2)

light1 = pygame.image.load("assets/light.png")
light1_rect = light1.get_rect()

light2 = pygame.image.load("assets/light.png")
light2_rect = light2.get_rect()

coin = pygame.image.load("assets/coin.png")
coin_rect = coin.get_rect()
coin_rect.center = (random.randint(0, screen_width), random.randint(text_size * 2, screen_height))

# else variables
fps = 60
clock = pygame.time.Clock()
game_is_running = True
speed = 5

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# timer
fps_time = 0
time = 100

# text variables
score_jedi = 0
score_sith = 0

# text
star_wars_font = pygame.font.Font("fonts/Starjedi.ttf", text_size)

score_jedi_text = star_wars_font.render(f"Jedi's score: {score_jedi}", True, black, white)
score_jedi_text_rect = score_jedi_text.get_rect()
score_jedi_text_rect.topleft = (0, 0)

score_sith_text = star_wars_font.render(f"Siths's score: {score_sith}", True, black, white)
score_sith_text_rect = score_sith_text.get_rect()
score_sith_text_rect.topright = (screen_width, 0)

time_text = star_wars_font.render(f"{time}", True, black, white)
time_text_rect = time_text.get_rect()
time_text_rect.midtop = (screen_width // 2, 0)

# sith moving variables
finishx = random.randint(64, screen_width)
finishy = random.randint(64, screen_height)

# sound
coin_sound = pygame.mixer.Sound("sound/coin.mp3")
lightsaber_sound = pygame.mixer.Sound("sound/lasrhit2.WAV")

pygame.mixer.music.load("sound/soundtrack.mp3")
pygame.mixer.music.play(-1, 0.0)

# game loop
while game_is_running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # if Q pressed:
            if event.key == pygame.K_q:
                game_is_running = False

    # jedi moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and jedi_rect.top >= text_size * 2:
        jedi_rect.y -= speed
    if keys[pygame.K_s] and jedi_rect.bottom <= screen_height:
        jedi_rect.y += speed
    if keys[pygame.K_a] and jedi_rect.left >= 0:
        jedi_rect.x -= speed
    if keys[pygame.K_d] and jedi_rect.right < screen_width:
        jedi_rect.x += speed

    # sith moving
    if keys[pygame.K_UP] and sith_rect.top >= text_size * 2:
        sith_rect.y -= speed - 1
    if keys[pygame.K_DOWN] and sith_rect.bottom <= screen_height:
        sith_rect.y += speed - 1
    if keys[pygame.K_LEFT] and sith_rect.left >= 0:
        sith_rect.x -= speed - 1
    if keys[pygame.K_RIGHT] and sith_rect.right < screen_width:
        sith_rect.x += speed - 1

    # light pose
    light1_rect.center = sith_rect.center
    light2_rect.center = jedi_rect.center

    # background is red
    screen.fill((255, 10, 10))

    # collision
    if sith_rect.colliderect(jedi_rect):
        lightsaber_sound.play()
        score_sith += 1
        score_sith_text = star_wars_font.render(f"Siths's score: {score_sith}", True, black, white)
        score_sith_text_rect = score_sith_text.get_rect()
        score_sith_text_rect.topright = (screen_width, 0)
        screen.blit(score_jedi_text, score_sith_text_rect)
        pygame.display.update()
        pygame.time.delay(1000)
        sith_rect.topleft = (0, 60)
        jedi_rect.center = (screen_width // 2, screen_height // 2)

    if jedi_rect.colliderect(coin_rect):
        coin_sound.play()
        coin_rect.center = (random.randint(0, screen_width), random.randint(text_size * 2, screen_height))
        score_jedi += 1
        score_jedi_text = star_wars_font.render(f"Jedi's score: {score_jedi}", True, black, white)
        score_jedi_text_rect = score_jedi_text.get_rect()
        score_jedi_text_rect.topleft = (0, 0)

    # time
    fps_time += 1

    if time == 0:
        time_text = star_wars_font.render(f"GAME ovER", True, black, white)
        time_text_rect = time_text.get_rect()
        time_text_rect.midtop = (screen_width // 2, 0)
        screen.blit(time_text, time_text_rect)
        screen.blit(coin, coin_rect)

        screen.blit(jedi, jedi_rect)
        screen.blit(sith, sith_rect)

        screen.blit(score_jedi_text, score_jedi_text_rect)
        screen.blit(score_sith_text, score_sith_text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        game_is_running = False

    if fps_time == fps:
        time -= 1
        fps_time = 0
        time_text = star_wars_font.render(f"{time}", True, black, white)
        time_text_rect = time_text.get_rect()
        time_text_rect.midtop = (screen_width // 2, 0)

    # you can see images
    screen.blit(coin, coin_rect)

    screen.blit(jedi, jedi_rect)
    screen.blit(sith, sith_rect)

    # you can see text
    screen.blit(score_jedi_text, score_jedi_text_rect)
    screen.blit(score_sith_text, score_sith_text_rect)

    screen.blit(time_text, time_text_rect)

    # update
    pygame.display.update()

    # fps
    clock.tick(fps)

# end of game
pygame.quit()
sys.exit()