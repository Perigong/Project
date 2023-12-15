import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Star Defense")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, enemies, bullets)
            controls.update_bullets(screen, stats, sc, enemies, bullets)
            controls.update_enemies(stats, screen, sc, gun, enemies, bullets)
run()
