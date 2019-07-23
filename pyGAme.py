import pygame
#from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()


size = (width,height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 255, 0)

fish_image = pygame.image.load("dvd2.png")
#fish_image = pygame.tarnsform.smoothscale(fish_image,(80,80))
fish_rect = fish_image.get_rect()

fish_rect = fish_image.get_rect()

fish_rect.center = (width//2,height//2)

speed=pygame.math.Vector2(2,-1)


def movefish():
    global color
    size = (width, height) = (int(screen_info.current_w), int (screen_info.current_h))
    fish_rect.move_ip(speed)

    if fish_rect.left < 0 :
        speed [0] *= -1
        color = (0, 255, 0)
    if fish_rect.right > width :
        speed [0] *= -1
        color = (255, 255, 0)
    if fish_rect.top < 0 :
        speed [1] *= -1
        color = (255, 255, 255)
    if fish_rect.bottom > height:
        speed [1] *= -1
        color = (0, 0, 0)
    if fish_rect.bottom > height:

        color = (0, 0, 0)


def main():
    while True:
        clock.tick(60)
        movefish()
        screen.fill(color)
        screen.blit(fish_image,fish_rect)
        pygame.display.flip()
if __name__ == "__main__":
     main()