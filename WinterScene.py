import pygame as p
import random


def setup():
    global screen, clock
    p.init()
    screen = p.display.set_mode((0, 0), p.FULLSCREEN)
    clock = p.time.Clock()


def main():
    done = False
    snowFlakes = []
    santaImg = p.image.load("images/reinder-image.jpg")  # it returns a Surface object
    scaleFactor = 0.75
    santaImg = p.transform.scale(santaImg, (int(santaImg.get_width() * scaleFactor),
                                            int(santaImg.get_height() * scaleFactor)))  # resize original image to 0.75X
    # santaImg = p.transform.scale(santaImg, (screen.get_width(),screen.get_height()*0.75))  # set image to size (screen_width , 0.75 * screen_height)
    santaX = -santaImg.get_width()
    santaVX = 30
    for i in range(500):
        x = random.randint(0, screen.get_width())
        y = random.randint(0, screen.get_height())
        r = random.randint(1, 5)
        snowFlakes.append((x, y, r))

    while not done:
        screen.fill(p.Color("lightskyblue"))
        # go through the event queue
        for e in p.event.get():
            if e.type == p.QUIT or (e.type == p.KEYDOWN and e.key == p.K_ESCAPE):
                done = True
        screen.blit(santaImg, (santaX, 100))
        if (santaX > screen.get_width() and santaVX > 0) or (santaX < -santaImg.get_width() and santaVX< 0):

            santaVX = -santaVX
            santaImg = p.transform.flip(santaImg, True, False)
            scaleFactor = 0.8
            santaImg = p.transform.scale(santaImg, (int(santaImg.get_width() * scaleFactor),
                                                    int(santaImg.get_height() * scaleFactor)))  # resize original image to 0.75X

        santaX += santaVX

        p.draw.rect(screen, p.Color("snow"),
                    p.Rect(0, 0.75 * screen.get_height(), screen.get_width(), 0.25 * screen.get_height()))
        for i in range(len(snowFlakes)):
            snowFlake = snowFlakes[i]
            snowFlakes[i] = (snowFlake[0] + random.randint(-1, 1), snowFlake[1] + random.randint(1, 4), snowFlake[2])

            p.draw.circle(screen, p.Color("snow2"), (snowFlake[0], snowFlake[1]), snowFlake[2])
            if snowFlake[1] > screen.get_height():
                snowFlakes[i] = (snowFlake[0], 0, snowFlake[2])  # reset the snowflake back to the top

        p.display.flip()  # redraws the display
        clock.tick(30)  # max out af 30 fps


setup()
main()
