import pygame
from sys import exit
import random

pygame.init()
#sc

scw, sch = 500, 500
sc=pygame.display.set_mode((scw,sch))
ett=random.randint(50,200)
två=random.randint(50,200)
tre=random.randint(50,200)
pygame.display.set_caption(" ")
gr = False


#svart
svart = pygame.image.load("¤/svart.png")
svart_r = svart.get_rect(center = (scw/2+100, sch/2))
pil_s = pygame.image.load("¤/pil_s.png")
pil_s_r = pil_s.get_rect(center = (scw/2+100, sch/2-50))
svartw, svarth = 20, 20
o = 0
svart_p = 0
psn = 0

#vit
vit = pygame.image.load("¤/vit.png")
pil_v = pygame.image.load("¤/pil_v.png")
pygame.display.set_icon(vit)
vit_r = vit.get_rect(center = (scw/2-100, sch/2))
vitw, vith = 20, 20
v = 67674573
vit_p = 0
pvn = 0

#text
font = pygame.font.SysFont("monospace", 11)
font2 = pygame.font.SysFont("monospace", 20)

def svart_m():
    if pygame.key.get_pressed()[pygame.K_RIGHT] and svart_r.x <= scw-svartw:
        svart_r.x += 2
    if pygame.key.get_pressed()[pygame.K_LEFT] and svart_r.x >= scw-scw:
        svart_r.x -= 2
    if pygame.key.get_pressed()[pygame.K_DOWN] and svart_r.y <= sch-svarth:
        svart_r.y += 2
    if pygame.key.get_pressed()[pygame.K_UP] and svart_r.y >= sch-sch:
        svart_r.y -= 2

def vit_m():
    if pygame.key.get_pressed()[pygame.K_d] and vit_r.x <= scw-vitw:
        vit_r.x += 2
    if pygame.key.get_pressed()[pygame.K_a] and vit_r.x >= scw-scw:
        vit_r.x -= 2
    if pygame.key.get_pressed()[pygame.K_s] and vit_r.y <= sch-svarth:
        vit_r.y += 2
    if pygame.key.get_pressed()[pygame.K_w] and vit_r.y >= sch-sch:
        vit_r.y -= 2


    


def måla():
    global timett, o, timet, ett, två, tre, pil_s, pil_v, psn, pvn
    if gr == True:
        text3 = font.render(str(vit_p), 1, (0, 0, 0))
        text3_r = text3.get_rect(topleft=(10, 10))
        text4 = font.render(str(svart_p), 1, (0, 0, 0))
        text4_r = text4.get_rect(topright=(scw-10, 10))
        text5 = font2.render(str(timet), 1, (0, 0, 0))
        text5_r = text5.get_rect(center=(scw/2, 15))  
        sc.fill((ett,två,tre))
        sc.blit(svart,svart_r)
        sc.blit(vit,vit_r)
        sc.blit(text3, text3_r)
        sc.blit(text4, text4_r)
        sc.blit(text5, text5_r)

        timett -= 0.0155
        timet = int(timett)
        if timet <= 0:
            svart_r.center = (scw/2+100, sch/2)
            vit_r.center = (scw/2-100, sch/2)
            timett = 11
            o += 1
            if o > 1:
                o = 0
        if o == 0:
            psn += 0.02
            if int(psn) == 0:
                pil_s_r = pil_s.get_rect(center = (scw/2+100, sch/2-50))
                sc.blit(pil_s, pil_s_r)
            elif int(psn) != 0:
                sc.fill((ett,två,tre))
                sc.blit(svart,svart_r)
                sc.blit(vit,vit_r)
                sc.blit(text3, text3_r)
                sc.blit(text4, text4_r)
                sc.blit(text5, text5_r)
                
        if o == 1:
            pvn += 0.02
            if int(pvn) == 0:
                pil_v_r = pil_v.get_rect(center = (scw/2+-100, sch/2-50))
                sc.blit(pil_v, pil_v_r)
            elif int(psn) != 0:
                sc.fill((ett,två,tre))
                sc.blit(svart,svart_r)
                sc.blit(vit,vit_r)
                sc.blit(text3, text3_r)
                sc.blit(text4, text4_r)
                sc.blit(text5, text5_r)


    else:
        sc.fill((ett,två,tre))
        text1 = font.render("WASD           <^>", 1, (0, 0, 0))
        text1_r = text1.get_rect(center=(scw/2, sch/2))
        text2 = font.render("Press {Space}", 1, (0, 0, 0))
        text2_r = text2.get_rect(midtop=(scw/2, sch/2-100))
        sc.blit(text1, text1_r)
        sc.blit(text2, text2_r)
        
timet = 0  
timett = 11

while True:
    t_time = pygame.time.get_ticks()
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    svart_m()
    vit_m()
    
        
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        gr = True

    if svart_r.colliderect(vit_r):
        if o == 0:
            svart_r.center = (scw/2+100, sch/2)
            vit_r.center = (scw/2-100, sch/2)
            o = 1
            svart_p += 1
            timett = 11
        elif o == 1:
            svart_r.center = (scw/2+100, sch/2)
            vit_r.center = (scw/2-100, sch/2)
            o=0
            vit_p += 1
            timett = 11

    måla()
    pygame.display.update()
    pygame.time.Clock().tick(60)