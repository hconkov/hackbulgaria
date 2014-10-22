class Cashdesk(object):

    def __init__(self, money):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def takemoney(self, takenmoney):
        for key in takenmoney:
            self.money[key] += takenmoney[key]

    def total(self):
        total = 0
        for key in self.money:
            total += self.money[key] * key
        return(total)

    def can_withdraw_money(self, amount_of_money):
        print self.total
        if amount_of_money > self.total:
            return(False)
        else:
            return(True)


cashdesk = Cashdesk()
cashdesk.takemoney({1: 2, 50: 1, 20: 1})
cashdesk.total()
print(cashdesk.total())
print(cashdesk.can_withdraw_money(74))
