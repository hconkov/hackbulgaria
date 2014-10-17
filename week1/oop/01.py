class cashdesk(object):

    def __init__(self, money):
        self.money = {100: 0, 50: 0, 20: 0, 10: , 5: 0, 2: 0, 1: 0}

    def takemoney(self):
        for key in self.money:
            