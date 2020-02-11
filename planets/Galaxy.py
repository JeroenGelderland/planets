from planets.Planet import Planet


class Galaxy:

    def __init__(self):
        self.planets = []

        self.planets.append(Planet("Mars", "red", 33, 33, 4))
        self.planets.append(Planet("Aarde", "blue", 45, 50, 84))

    def movePlanets(self):
        average_x = sum([planet.x for planet in self.planets]) / len(self.planets)
        average_y = sum([planet.y for planet in self.planets]) / len(self.planets)

        for planet in self.planets:
            planet.move(average_x, average_y)
            planet.resize()
