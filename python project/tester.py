import pygame as pg
import random

pg.init()
pg.display.set_caption('basket catch!')
width, height = 900, 500
root = pg.display.set_mode((width, height))
white = (255, 255, 255)
black = (0, 0, 0)
fps = 45
vel = 15
fall = 10

def draw_window(basket, balls):
    root.fill(white)
    pg.draw.rect(root, black, basket)
    
    # Loop through the list and draw every ball
    for ball in balls:
        pg.draw.circle(root, black, (ball.x, ball.y), 15)
        
    pg.display.update()

def main():
    clock = pg.time.Clock()
    basket = pg.Rect(width // 2 - 30, 480, 75, 20)
    
    # 1. Create a list to hold all the balls
    balls = []
    total_balls_to_spawn = 30
    balls_spawned = 0
    
    # 2. Set up a custom timer event to spawn a ball every 1000 milliseconds (1 second)
    SPAWN_BALL = pg.USEREVENT + 1
    pg.time.set_timer(SPAWN_BALL, 1000) 

    run = True
    while run:
        clock.tick(fps)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
            # Listen for the timer event
            if event.type == SPAWN_BALL and balls_spawned < total_balls_to_spawn:
                # Generate a random x coordinate within the screen bounds
                random_x = random.randint(20, width - 20)
                new_ball = pg.Rect(random_x, 0, 17, 17)
                balls.append(new_ball)
                balls_spawned += 1

        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_LEFT] and basket.x - vel > 0:
            basket.x -= vel
        if key_pressed[pg.K_RIGHT] and basket.x + vel + basket.width < width:
            basket.x += vel
            
        # 3. Update the y-coordinate (trajectory) for every ball in the list
        for ball in balls:
            ball.y += fall
            
        draw_window(basket, balls)

    pg.quit()

if __name__ == '__main__':
    main()
























































