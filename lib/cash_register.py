#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        # update total
        self.total += price * quantity

        # add items multiple times
        for _ in range(quantity):
            self.items.append(item)

        # store transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)
        self.total = round(self.total, 2)

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # remove from total
        self.total -= last["price"] * last["quantity"]

        # remove items
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])

        # prevent negative float issues
        if self.total < 0:
            self.total = 0.0