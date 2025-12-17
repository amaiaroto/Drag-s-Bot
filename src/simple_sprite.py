import pygame


class SimpleSprite:
    def __init__(self, image, is_draggable=False):
        self.x: int = 0
        self.y: int = 0
        self.image = image
        self.draggable: bool = is_draggable
        self.pos = (self.x, self.y)

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
        screen.blit(self.image, (self.x, self.y))

    def get_rect_snaps(self):
        r=self.get_rect()
        return [r.bottomright, r.topleft, r.bottomright, r.topleft, r.bottomright]
