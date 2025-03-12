# to start venv: source venv/bin/activate

import os
import sys
import time
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
    dead = False
    written = False
    asteroid_count = 0

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

    player, asteroidfield = initialize_game()

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
                for shot in shots:
                    shot.kill()
                asteroidfield.kill()
                player.kill()
                dead = True
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
            
            asteroid_count += 1
            if asteroid_count > 25:
                asteroid.kill_on_edge()
        asteroid_count = 0
        
        for wrap in wrappable:
            wrap.wrap_around()

        for draw in drawable:
            screen.blit(score_text, (10, 10))        
            draw.draw(screen)

        if dead:
            display_score(score, screen, font)
            if not written:
                save_score(score)
                written = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r] and dead:
            print("Restarted the Game!")
            player, asteroidfield = reset_game(asteroids)
            dead = False
            score = 0
            written = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def initialize_game():
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    return player, asteroidfield

def reset_game(asteroids):
    for asteroid in asteroids:
        asteroid.kill()
    return initialize_game()


def display_score(score, screen, font):
    try:
        with open("high_score.txt", "r") as file:
            high_score = file.read()
    except FileNotFoundError:
        with open("high_score.txt", "w") as file:
            file.write("0")        
        with open("high_score.txt", "r") as file:
            high_score = file.read()
            
    game_over_text = font.render("GAME OVER!", True, (255, 255, 255))
    game_over_score = font.render(f"YOUR SCORE IS: {score}", True, (255, 255, 255))
    game_over_high_score = font.render(f"HIGH SCORE = {high_score}", True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT//2 - 100))
    screen.blit(game_over_score, (SCREEN_WIDTH//2 - 105, SCREEN_HEIGHT//2))
    screen.blit(game_over_high_score, (SCREEN_WIDTH//2 - 85, SCREEN_HEIGHT//2 + 100))

def save_score(score):
    if is_high_score(score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

def is_high_score(score):
    with open("high_score.txt", "r+") as file:
        try:
            if score > int(file.read()):
                return True
            return False
        except ValueError:
            file.write(str(score))

def fps_counter():
    timer = time.time()

if __name__ == "__main__":
    main()