try:
    import pygame as pg
    from simple_sprite import SimpleSprite
    from simple_sprite import SimpleSprite
    import numpy as np
    from random import Random, choice

except ImportError:
    exit('Failed to load libraries') if __name__ == '__main__' else None
    import pygame as pg
    from simple_sprite import SimpleSprite
    from simple_sprite import SimpleSprite
    import numpy as np
    from random import Random, choice

window_width = 800
window_height = 600
drawer_height = 50
ex = '.png'
robot_pos = (0, 0)

def get_asset_path(name,extension=ex):
    return "../assets/" + name+extension

screen = pg.display.set_mode((window_width, window_height))

list_of_strings = ['circle1', 'circle', 'iliketomoveit-removebg-preview']
robot = ['banban']
list_of_strings = map(lambda x: get_asset_path(x), list_of_strings)
robot = map(lambda x: get_asset_path(x), robot)

sprites = [SimpleSprite(pg.image.load(s)) for s in list_of_strings]
robot = [SimpleSprite(pg.image.load(i)) for i in robot]
pg.display.set_caption('Simple Drag')
pg.display.set_icon(pg.image.load(get_asset_path('not ready yet-1.png')))
padding = 12
core = robot[0]

for s in sprites:
    s.scale_by_height(drawer_height)

for i in robot:
    i.scale_by_width(drawer_height)
    i.move_to(window_width / 2, window_height / 2, center=True)

drag_started = None
dragged_sprite = None

# Randomize the order
if True:
    a = Random()
    a.shuffle(sprites)

positions = {}


def draw_part_drawer(sprite: list[SimpleSprite], x, y):
    global padding

    for s in sprite:
        s.move_to(x, y - padding)
        positions[s] = (s.x, s.y)

        # Move to next sprite position
        x += s.image.get_width() + padding


draw_part_drawer(sprites, padding, window_height - drawer_height)
clock = pg.time.Clock()

dt = 0
speed = 125
while True:
    loop_speed = speed * dt
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

    if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
        for s in robot:
            s.move_by(0, -loop_speed)

    if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
        for s in robot:
            s.move_by(0, loop_speed)

    if pg.key.get_pressed()[pg.K_RIGHT] or pg.key.get_pressed()[pg.K_d]:
        for s in robot:
            s.move_by(loop_speed, 0)

    if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_a]:
        for s in robot:
            s.move_by(-loop_speed, 0)

    if pg.mouse.get_pressed()[0]:
        if drag_started and dragged_sprite:
            dragged_sprite.move_by(*np.subtract(pg.mouse.get_pos(), drag_started))

        else:
            for s in sprites:
                if s.get_rect().collidepoint(pg.mouse.get_pos()):
                    dragged_sprite = s

                    break

        drag_started = pg.mouse.get_pos()

    else:
        if dragged_sprite is not None:
            for i in core.get_rect_snaps():
                print(i)
                if dragged_sprite.get_rect().collidepoint(*i):
                    sprites.remove(dragged_sprite)
                    robot.append(dragged_sprite)
                    dragged_sprite.move_to(*choice(core.get_rect_snaps()))

                else:
                    dragged_sprite.move_to(*positions[dragged_sprite])

        drag_started = None
        dragged_sprite = None

    #     stick part here

    # TODO: add movement to body + stuck part (another list of body+stuck parts)

    screen.fill((180, 160, 255))

    for s in sprites:
        s.draw(screen)

    for i in robot:
        i.draw(screen)

    pg.display.flip()
    snap_points = core.get_rect()

    dt = clock.tick(60) / 1000
