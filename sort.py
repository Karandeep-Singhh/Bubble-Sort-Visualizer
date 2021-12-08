import pygame
import random
pygame.init()

WIDTH, HEIGHT = 1200, 600

WHITE = (240, 240, 240)
BLACK = (240, 240, 240)
BAR_COLOR = (102, 0, 204)
SELECTED_COLOR = (0, 155, 155)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort")
font = pygame.font.SysFont("comicsans", 20)
INPUT_LENGTH = 80
GREEN = (70, 150, 0)


class Bars:
    def __init__(self, col, gap, inp_length):
        self.height = inp_length
        self.col = col
        self.x = gap*col
        self.color = BAR_COLOR
        self.y = HEIGHT - inp_length
        self.width = gap

    def fillBars(self):
        pygame.draw.rect(
            WIN, self.color, (self.x, self.y, self.width, self.height))

    def setVal(self):
        txt = font.render(str(self.height), 1, (0, 0, 0))
        txt = pygame.transform.rotate(txt, 90)
        WIN.blit(txt, (self.x, self.y - txt.get_height()))


def sort(draw, bars, inputs):
    clock = pygame.time.Clock()
    varr = INPUT_LENGTH
    for i in range(INPUT_LENGTH):
        varr -= 1
        for j in range(varr):
            # clock.tick(120)
            bars[j].color = SELECTED_COLOR

            if bars[j].height > bars[j+1].height:

                bars[j].x, bars[j+1].x = bars[j+1].x, bars[j].x
                bars[j], bars[j+1] = bars[j+1], bars[j]
                bars[j].color = BAR_COLOR
            draw()

    for bar in bars:
        bar.color = GREEN
        draw()


def makeBars(inputs):
    bars = []
    gap = WIDTH//INPUT_LENGTH
    for i in range(INPUT_LENGTH):
        bar = Bars(i, gap, inputs[i])
        bars.append(bar)
    return bars


def drawColumns():
    gap = WIDTH//INPUT_LENGTH

    for i in range(INPUT_LENGTH):
        pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, HEIGHT))


def draw(bars):
    WIN.fill(WHITE)

    for bar in bars:
        bar.fillBars()
    for bar in bars:
        bar.setVal()
    drawColumns()
    pygame.display.update()


def play():

    run = True
    inputs = [random.randrange(10, HEIGHT-20, 1) for i in range(INPUT_LENGTH)]
    bars = makeBars(inputs)
    clock = pygame.time.Clock()
    while run:
        # clock.tick(4)
        draw(bars)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    # randomize inputs
                    inputs = [random.randint(10, 500)
                              for i in range(INPUT_LENGTH)]
                    bars = makeBars(inputs)

                if e.key == pygame.K_SPACE:
                    sort(lambda: draw(bars), bars, inputs)


play()
