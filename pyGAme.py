import sys,pygame
#from pygame.locals import *

pygame.init()
#screen_info = pygame.display.info()


screen = pygame.display.set_mode(200,int(screen_info.current_h))
clock = pygame.time.Clock()


def main():
    while True:
        clock.tick(60)
        screen.fill(0,140,200)
        pygae.display.flip()
if __name__ == "__main__":
     main()