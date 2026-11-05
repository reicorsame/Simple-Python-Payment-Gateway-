
class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Processing a credit card payment of ${amount}")


class DigitalWallet(PaymentMethod):
    def pay(self, amount):
        print(f"Routing ${amount} through digital wallet")


def process_checkout(payment_method, amount):
    payment_method.pay(amount)


payments = [
    CreditCard(),
    DigitalWallet(),
    CreditCard()
]

remaining_amounts = [500, 300, 200]

for payment, amount in zip(payments, remaining_amounts):
    process_checkout(payment, amount)
