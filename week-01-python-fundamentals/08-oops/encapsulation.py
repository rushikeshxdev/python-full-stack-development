# ==========================================================
# OOP - Encapsulation
# ==========================================================
#
# THEORY:
#
# Encapsulation means keeping data and the methods that operate
# on that data together and controlling how that data is accessed.
#
# Python commonly uses:
#
# _name
#     Convention: internal/protected-style attribute
#
# __name
#     Name-mangled attribute
#
# A common approach is to expose controlled methods for updating
# internal state.
#
# ==========================================================


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount


account = BankAccount("Rushikesh", 1000)

print("Balance:", account.get_balance())

account.deposit(500)
print("After deposit:", account.get_balance())

account.withdraw(300)
print("After withdrawal:", account.get_balance())