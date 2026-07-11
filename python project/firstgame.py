import pygame as pg
import os
pg.init()
WIDTH, HEIGHT = 900, 500
root = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('First Game ⚔⚔⚔⚔⚔⚔⚔⚔⚔')
FPS=60
vel=5
max_bullets=3

yellow_hit=pg.USEREVENT+1
red_hit=pg.USEREVENT+2



border=pg.Rect(WIDTH//2 - 5,0,10,HEIGHT)
black=(0,0,0)

bullet_vel=7
spaceship_width,spaceship_height=55,40
y_spaceship_image=pg.image.load(os.path.join('Assets','spaceship_yellow.png'))
y_spaceship=pg.transform.rotate(pg.transform.scale(y_spaceship_image,(spaceship_width,spaceship_height)),90)
r_spaceship_image=pg.image.load(os.path.join('Assets','spaceship_red.png'))
r_spaceship=pg.transform.rotate(pg.transform.scale(r_spaceship_image,(spaceship_width,spaceship_height)),270)




def draw_window(red,yellow,red_bullets,yellow_bullets):
    root.fill((255,255,255))
    pg.draw.rect(root,black,border)
    root.blit(y_spaceship,(yellow.x,yellow.y))
    root.blit(r_spaceship,(red.x,red.y))
    for bullet in red_bullets:
        pg.draw.rect(root,(255,0,0),bullet)
    for bullet in yellow_bullets:
        pg.draw.rect(root,(255,255,0),bullet)
    
    pg.display.update()
    

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pg.K_a] and yellow.x-vel>0:
        yellow.x-=vel
    if key_pressed[pg.K_d] and yellow.x+vel+yellow.width<border.x:
        yellow.x+=vel
    if key_pressed[pg.K_w] and yellow.y-vel>0:
        yellow.y-=vel
    if key_pressed[pg.K_s] and yellow.y+vel+yellow.height<HEIGHT-15:
        yellow.y+=vel
 

def red_handle_movement(key_pressed,red):
    if key_pressed[pg.K_LEFT] and red.x-vel>border.x+border.width:
        red.x-=vel
    if key_pressed[pg.K_RIGHT] and red.x+vel+red.width<WIDTH:
        red.x+=vel
    if key_pressed[pg.K_UP] and red.y-vel>0:
        red.y-=vel
    if key_pressed[pg.K_DOWN] and red.y+vel+red.height<HEIGHT-15:
        red.y+=vel

def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for bullet in yellow_bullets:
        bullet.x+=bullet_vel
        if red.colliderect(bullet):
            pg.event.post(pg.event.Event(red_hit))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x-=bullet_vel
        if yellow.colliderect(bullet):
            pg.event.post(pg.event.Event(yellow_hit))
            red_bullets.remove(bullet)







def main():
    red=pg.Rect(700,300,spaceship_width,spaceship_height)
    yellow=pg.Rect(100,300,spaceship_width,spaceship_height)
    clock=pg.time.Clock()
    run = True
    red_bullets=[]
    yellow_bullets=[]
    
    
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LCTRL and len(yellow_bullets)<max_bullets:
                bullet=pg.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                yellow_bullets.append(bullet)
            if event.key==pg.K_RCTRL and len(red_bullets)<max_bullets:
                bullet=pg.Rect(red.x,red.y+red.height//2-2,10,5)
                red_bullets.append(bullet)
   
        
        
        
        
        key_pressed=pg.key.get_pressed()
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        handle_bullets(red_bullets,yellow_bullets,red,yellow)
        
        
        draw_window(red,yellow,red_bullets,yellow_bullets)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pg.quit()


if __name__ == '__main__':
    main()