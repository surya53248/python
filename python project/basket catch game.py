import pygame as pg
pg.init()
pg.display.set_caption('basket catch!')
width,height=900,500
root=pg.display.set_mode((width,height))
white=(255,255,255)
fps=45
black=(0,0,0)
vel=15
fall=10


def draw_window(basket,circle_rect):
    root.fill(white)
    pg.draw.rect(root,black,basket)
    pg.draw.circle(root,black,(circle_rect.x,circle_rect.y),15)
    pg.display.update()
  


def main():
    clock=pg.time.Clock()
    basket=pg.Rect(width//2-30,480,65,20)
    circle_rect=pg.Rect(20,200,17,17)
    run=True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
        key_pressed=pg.key.get_pressed()
        if key_pressed[pg.K_LEFT] and basket.x-vel>0:
            basket.x-=vel
        if key_pressed[pg.K_RIGHT] and basket.x+vel+basket.width<width:
            basket.x+=vel
        circle_rect.y+=fall
        

        
        draw_window(basket,circle_rect)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pg.quit()


if __name__=='__main__':
    main()