import pygame
from Host import main as Host

X = 800
Y = 800
FILE_STRT = r'strt_alpha.png'
TITLE = "KAHOOT"
def main():
    pygame.init()

    # define the RGB value
    # for white colour
    white = (255, 255, 255)

    # assigning values to X and Y variable

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption(TITLE)

    # create a surface object, image is drawn on it.
    image = pygame.image.load(FILE_STRT)

    # infinite loop
    while True:

        # completely fill the surface object
        # with white colour
        display_surface.fill(white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0]>= 253 and pos[0]<=471 and pos[1]>= 265 and pos[1]<=408:
                    Host()
                elif pos[0]>= 253 and pos[0]<=471 and pos[1]>= 499 and pos[1]<=643:
                    print("boolik")






            # Draws the surface object to the screen.
            pygame.display.update()

if __name__ == '__main__':
    main()
