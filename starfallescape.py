import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
ROCKET_IMG = pygame.image.load("rocket.png")
ROCKET = pygame.transform.scale(ROCKET_IMG, (60, 90))

STAR_IMG = pygame.image.load("star.png")  # Load star image
STAR_WIDTH, STAR_HEIGHT = 40, 40
STAR_VEL = 7

FONT = pygame.font.SysFont("comicsans", 30)

def draw_star(surface, x, y):
    scaled_star = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))
    surface.blit(scaled_star, (x, y))

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(ROCKET, (player.x, player.y))

    for star in stars:
        draw_star(WIN, star.x, star.y)

    pygame.display.update()

def add_stars(stars, row_count):
    star_positions = []
    for row in range(row_count):
        for _ in range(10):
            star_x = random.randint(0, WIDTH - STAR_WIDTH)
            star_y = random.randint(-HEIGHT, -STAR_HEIGHT * 2) - row * STAR_HEIGHT * 2
            star_positions.append((star_x, star_y))

    for pos in star_positions:
        star = pygame.Rect(pos[0], pos[1], STAR_WIDTH, STAR_HEIGHT)
        stars.append(star)

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - 60, 40, 60)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            add_stars(stars, 2)  # Add stars in 2 rows
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - 5 >= 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.x + 5 + player.width <= WIDTH:
            player.x += 5

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()
