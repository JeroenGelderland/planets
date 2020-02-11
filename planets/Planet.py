from random import Random

COLORS = ('red', 'blue', 'green', 'purple', 'yellow', 'pink',
          'brown', 'magenta', 'black', 'white')

MAX_POS = 100
MIN_POS = 0
RANDOM = Random()


class Planet:

    def __init__(self, name, color, radius, x, y):
        self.naam = name
        self.radius = radius

        if COLORS.__contains__(color):
            self.color = color
        else:
            raise ValueError('Color is invalid')

        if MIN_POS <= x <= MAX_POS and MIN_POS <= y <= MAX_POS:
            self.x = x
            self.y = y
        else:
            raise ValueError('Position is invalid')

    def resize(self):
        self.radius += RANDOM.randint(-2, 2)

    def move(self, x_speed, y_speed):
        self.x += x_speed
        self.y += y_speed

        if MIN_POS < self.x:
            self.x = MIN_POS
        if MAX_POS > self.x:
            self.x = MAX_POS
        if MIN_POS < self.y:
            self.y = MIN_POS
        if MAX_POS > self.y:
            self.y = MAX_POS
