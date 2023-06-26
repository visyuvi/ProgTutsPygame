import pygame as p


def setup():
    global screen
    global clock
    p.init()
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()


def main():
    done = False
    isBlue = True
    while not done:
        screen.fill((0, 0, 0))
        # go through the event queue
        for e in p.event.get():
            if e.type == p.QUIT:
                done = True

            if e.type == p.KEYDOWN and e.key == p.K_DOWN:
                isBlue = not isBlue
        if isBlue:
            color = (56, 82, 186)  # 0 - 255
        else:
            color = (160, 50, 50)
        rectangle1 = p.Rect(0, 0, 50, 50)
        p.draw.rect(screen, color, rectangle1)  # x, y, width, height
        p.display.flip()  # redraws the display
        clock.tick(30)  # max out af 30 fps


setup()
main()
