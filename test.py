import pygame
import pygame.locals as pl

if __name__ == '__main__':
    pygame.init()
    pygame.key.set_mods(0) # 한글 입력 방식 변경

    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.SysFont('malgungothic', 36)

    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pl.KEYDOWN:
                if event.key == pl.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pl.K_RETURN:
                    print(input_text)
                    input_text = ""
                else:
                    input_text += event.unicode

        screen.fill((255, 255, 255))
        text = font.render(input_text, True, (0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()