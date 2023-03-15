import pygame, math, time, os, random

w = 1600
h = w * (9 / 16)

screen = pygame.display.set_mode((w, h))

main = True
ingame = True

t1, t2, t3, t4 = [], [], [], []



while main:
    while ingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        screen.fill((0, 0, 0))

        # gear background
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - w*(4/10), -int(w/100), w*(8/10), h + int(w / 50)))
        
        # gear line
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w*(4/10), -int(w/100), w*(8/10), h + int(w / 50)), int(w / 200))

        # note
        # 100, 200, 300, 400 부분을 tile_data[0] - h / 100으로 수정해야 함
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w*(4/10), 100, w*(2/10), h / 50))
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w*(2/10), 200, w*(2/10), h / 50))
        pygame.draw.rect(screen, (255, 255, 255), (w/2           , 300, w*(2/10), h / 50))
        pygame.draw.rect(screen, (255, 255, 255), (w/2 + w*(2/10), 400, w*(2/10), h / 50))
        
        # 판정선
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - w*(4/10), (h/12) * 9, w*(8/10), h / 2))
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w*(4/10), (h/12) * 9, w*(8/10), h / 2), int(h / 100))

        # 버튼 이펙트
        # keys[0] 넣어야 함
        # for i in range(7):
        #     i += 1
        #     pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 12) * 9 - (h / 30) * keys[0] * i, w / 16 * keys[0], (h / 35) / i))
 


        # 버튼 꾸미기
        # 이펙트 주려면 keys[0] 넣어야 함
        pygame.draw.circle(screen, (255, 255, 255), (w/2 - w*(3/10), (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.circle(screen, (255, 255, 255), (w/2 - w*(1/10), (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.circle(screen, (255, 255, 255), (w/2 + w*(1/10), (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.circle(screen, (255, 255, 255), (w/2 + w*(3/10), (h / 24) * 21), (w / 20), int(h / 200))



    

        pygame.display.flip()
    

    main = False
    ingame = False