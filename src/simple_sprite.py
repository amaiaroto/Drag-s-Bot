import pygame


class SimpleSprite:
    def __init__(self, image, is_draggable=False):
        self.x: int = 0
        self.y: int = 0
        self.image = image
        self.draggable: bool = is_draggable
        self.snap_point = None

    def center_tuple(self,tuple):
        return tuple[0] - self.image.get_width() / 2, tuple[1] - self.image.get_height() / 2


    def move_to(self, x, y, center=False):
        self.x = x - (self.image.get_width() / 2 if center else 0)
        self.y = y - (self.image.get_height() / 2 if center else 0)

    def move_by(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def get_rect(self):
        return self.image.get_rect().move(self.x, self.y)

    def scale(self, factor):
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() / factor, self.image.get_height() / factor))

    def scale_by_width(self, wanted_width):
        factor = self.image.get_width() / wanted_width
        self.scale(factor)

    def scale_by_height(self, wanted_height):
        factor = self.image.get_height() / wanted_height
        self.scale(factor)

    def draw(self, screen):
        # change this to work in 2 ways:
        # if snap is present draw at snap point
        # else draw as we do now
        if self.snap_point is not None:
            screen.blit(self.image, self.center_tuple(self.snap_point))
            # screen.blit(self.image, self.snap_point)

        else:
            screen.blit(self.image, self.get_pos())

        for i in self.get_rect_snaps():
            pygame.draw.circle(screen, 'orange', i, 2)
        if self.snap_point is not None:
            pygame.draw.circle(screen, 'red', self.snap_point, 4)


    def get_rect_snaps(self):
        r = self.get_rect()
        return [r.topleft, r.topright, r.bottomright, r.bottomleft]

    def get_pos(self):
        return (self.x, self.y)

    def get_th(self):
        return 50
