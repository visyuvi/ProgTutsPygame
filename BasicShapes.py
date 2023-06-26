import pygame as p


def setup():
    global screen
    global clock
    p.init()
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()


def main():
    done = False

    while not done:
        screen.fill((0, 0, 0))
        # go through the event queue
        for e in p.event.get():
            if e.type == p.QUIT:
                done = True

        p.display.flip()  # redraws the display
        clock.tick(30)  # max out af 30 fps


setup()
main()
