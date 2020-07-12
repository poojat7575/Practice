class Money:
    def __init__(self, form, val):
        self.form = form
        self.val = int(val)


class Bag:
    def __init__(self):
        self.coins = []
        self.notes = []
    def add(self, money):
        if money.form == "Coin":
            self.coins.append(money)
        else:
            self.notes.append(money)
    def display(self):
        total_amount = 0
        for money in self.coins + self.notes:
            total_amount += money.val 
        print(total_amount)

if __name__ == "__main__":
    t = int(input())
    bag = Bag()
    for _ in range(t):
       bag.add(Money(*(input().split(' '))))
    print("Coins :")
    for money in bag.coins:
        print(money.val)
    
    print("Notes :")
    for money in bag.notes:
        print(money.val)

