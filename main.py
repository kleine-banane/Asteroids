# to start venv: source venv/bin/activate

import os
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    score = 0
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    wrappable = pygame.sprite.Group()

    Player.containers = (wrappable, updatable, drawable)
    Asteroid.containers = (wrappable, asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (wrappable, shots, updatable, drawable)    

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for update in updatable:
            update.update(dt)
            score_text = font.render(str(score), True, (255, 255, 255))

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                asteroidfield.kill()
                for asteroid in asteroids:
                    asteroid.kill()
                player.kill()
                game_over = font.render(f"Your score is: {score}!", True, (255, 255, 255))
                screen.blit(game_over, (SCREEN_HEIGHT/2, SCREEN_WIDTH/2))
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
        
        for wrap in wrappable:
            wrap.wrap_around()

        for draw in drawable:
            screen.blit(score_text, (10, 10))        
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()