import pygame
from random import randint

screen_size = [385,600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')

def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30 )
    score_text = 'Score: ' + str(score)
    text_img = font.render(score_text, True, (0,255,0))
    screen.blit(text_img, [20,10])

def random_offset():
  return -1 * randint(100,1200)


chicken_y = [random_offset(),random_offset(), random_offset()]
user_x = 160
score = 0

def crashed(idx):
    global score
    score -= 50
    print('crashed with chicken ', idx,score)
    chicken_y[idx] =random_offset()

def update_chicken_pos(idx):
  if chicken_y[idx] > 600:
    global score
    chicken_y[idx] = random_offset()
    score +=5
    print('Score',score)

  else:
    chicken_y[idx] +=5

keep_alive = True
clock= pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys= pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 300:
        user_x +=10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x -=10

    update_chicken_pos(0)
    update_chicken_pos(1)
    update_chicken_pos(2)

    screen.blit(background, [0, 0])
    screen.blit(user, [user_x, 520])
    screen.blit(chicken, [0, chicken_y[0]])
    screen.blit(chicken, [150, chicken_y[1]])
    screen.blit(chicken, [300, chicken_y[2]])

    if 550 > chicken_y[0] > 450 and user_x <80:
        crashed(0)

    if 550 > chicken_y[1] > 450 and 240 > user_x > 80: # and user_x < 240:
        crashed(1)

    if 550 > chicken_y[2] > 450 and user_x > 220:
        crashed(2)
    display_score(score)
    pygame.display.update()
    clock.tick(60)

# teste de commit


