class Issue:

    def __init__(self):
        self.x = 1
        self.y = [1, 2, 3]
        self.ca(self.x)
        self.cal(self.y)

    def ca(self, number):
        number += 1

    def cal(self, num_list):
        num_list[1] += 1
        num_list = num_list[1:]
