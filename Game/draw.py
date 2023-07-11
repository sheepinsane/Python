import pygame

# 初始化Pygame
pygame.init()
pixel_art = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]
pixel_art1 = [
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0]
]
pixel_art2 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
pixel_art3 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

pixieFPS = [pixel_art,pixel_art1,pixel_art2,pixel_art3]

pixieObj1 = [0,0]
pixieObj2 = [25,25]
pixieObj3 = [50,50]
pixieObj4 = [25,70]
pixieObj5 = [0,100]
pixieObject = [pixieObj1,pixieObj2,pixieObj3,pixieObj4,pixieObj5]

screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))

colors = {
    0: (0, 0, 0),   # 黑色
    1: (255, 255, 255)  # 白色
}

def DrawPixieFPS():
        for pixie in pixieFPS:
            DrawPixie(pixie)   
            pygame.time.delay(100)
            pygame.display.flip()               


def DrawPixie(pixel_art):
    screen.fill((0, 0, 0))
    for y, row in enumerate(pixel_art):
            for x, pixel in enumerate(row):
                color = colors[pixel]
                for obj in pixieObject:
                    pixel_rect = pygame.Rect(x * pixel_size + obj[0], y * pixel_size + obj[1], pixel_size, pixel_size)
                    pygame.draw.rect(screen, color, pixel_rect)
                
    


# 設置畫面的寬度和高度

pygame.display.set_caption("Pixel Art")

# 定義畫面中的點陣圖像素大小
pixel_size = 5

# 遊戲迴圈
running = True
blink = True
while running:
    
    DrawPixieFPS()
    # 檢查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 延遲一小段時間
    blink = not blink
    #pygame.time.delay(250)

# 關閉Pygame
pygame.quit()