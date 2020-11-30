import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('НЫААААААААААААА')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    pos = []
    x_down = []
    y_down = []
    n = 0
    fps = 30
    v = 100  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos.append([event.pos[0], event.pos[1]])
                x_down.append(False)
                y_down.append(False)
                n += 1
        try:
            for i in range(n):
                pygame.draw.circle(screen, 'white', pos[i], 10)
                if n > 1:
                    for j in range(n):
                        if abs(pos[i][0] - pos[j][0]) <= 10 and abs(pos[i][1] - pos[j][1]) <= 10:
                            pygame.mixer.Sound("3.mp3").play()
                            x_down[i] = not x_down[i]
                            y_down[i] = not y_down[i]
                            x_down[j] = not x_down[j]
                            y_down[j] = not y_down[j]
                if x_down[i] and pos[i][0] < width - 10:  # Обработка по x
                    pos[i][0] += v / fps
                else:
                    if pos[i][0] > 10:
                        x_down[i] = False
                        pos[i][0] -= v / fps
                    else:
                        x_down[i] = True

                if y_down[i] and pos[i][1] < height - 10:  # Обработка по y
                    pos[i][1] += v / fps
                else:
                    if pos[i][1] > 10:
                        y_down[i] = False
                        pos[i][1] -= v / fps
                    else:
                        y_down[i] = True
        except:
            screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(fps)
