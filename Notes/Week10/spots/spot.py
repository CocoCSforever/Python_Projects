class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        noStroke()

        # white
        fill(255)
        ellipse(self.x, self.y, 95, 95)

        # black
        fill(0)
        ellipse(self.x, self.y, 80, 80)

        fill(255)
        ellipse(self.x, self.y, 65, 65)

        # red
        fill(255, 0, 0)
        ellipse(self.x, self.y, 50, 50)

        fill(255)
        ellipse(self.x, self.y, 25, 25)

        fill(0)
        ellipse(self.x, self.y, 10, 10)
