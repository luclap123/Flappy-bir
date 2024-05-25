#Thư viện pygame
import pygame
# khởi tạo
pygame.init() 

p=0.15 #Hằng trọng lực
bird_y= 0 #Toạ độ y của bird
score=0 #Khoi tao diem
game_play = True # trạng thái game

#Score
game_font=pygame.font.Font('04B_19.TTF',40)
def score_view():
    score_f=game_font.render(str(int(score)), True, (255,255,255))
    score_hcn=score_f.get_rect(center=(200,100))
    screen.blit(score_f, score_hcn)
    
#Tiêu đề và icon game:
pygame.display.set_caption('Flappy Birds')
icon=pygame.image.load(r'assets\yellowbird-downflap.png')

#Thêm background cho game
bg=pygame.image.load(r'assets\background-night.png')
bg=pygame.transform.scale2x(bg)
fl=pygame.image.load(r'assets\floor.png')
fl=pygame.transform.scale2x(fl)
fl_x=0
pygame.display.set_icon(fl)

#Cửa sổ game
screen=pygame.display.set_mode((432,768))

#Bird
bird=pygame.image.load(r'assets\yellowbird-midflap.png')
bird=pygame.transform.scale2x(bird)
bird_hcn=bird.get_rect(center=(100,386))

# menu
screen_kt=pygame.image.load(r'assets\message.png')
screen_kt=pygame.transform.scale2x(screen_kt)
screen_kt_hcn=bird.get_rect(center=(100,300))

# kiểm tra va cham
def checkCollider():
    if (bird_hcn.bottom >= 668 or bird_hcn.top <=-75):
        return False
    else:
        return True

#Vòng lặp xử lý game
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_play:
                bird_y=-10
            if event.key==pygame.K_SPACE and game_play==False:
                game_play=True
                bird_y=0
                bird_hcn.center=(100, 336)
                
    # màn hinfnh chạy
    screen.blit(bg, (0,0))
    fl_x-=1
    screen.blit(fl,(fl_x,600))
    screen.blit(fl,(fl_x+432,600))
    if fl_x==-432:
        fl_x=0
        
    #Bird
    if game_play:
        screen.blit(bird, bird_hcn)
        bird_y+=p
        bird_hcn.centery+=bird_y
        score+=0.01
        score_view()
        game_play=checkCollider()
    else:
        screen.blit(screen_kt, screen_kt_hcn)
    pygame.display.update()